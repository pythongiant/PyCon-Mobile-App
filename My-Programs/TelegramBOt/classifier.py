from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import pandas
import datefinder
import webbrowser
import os

working_dir=os.getcwd()
with open(working_dir+'/train.csv', 'r') as train:
     classifier = NaiveBayesClassifier(train, format="csv")

class SandraBot():

    def returnObj(self,text,*args):
        df=pandas.read_csv(working_dir+"/meetings.csv",index_col=False)
        lang_df=pandas.read_csv(working_dir+"/Language.csv",index_col=False)

        blob=TextBlob(text)
        MeetingFile=open(working_dir+"/meetings.csv",'a')
        print(classifier.classify(text))
        MeetingFile.write("\n")
        #Algorithm to treat new meetings
        if classifier.classify(text) == 'meeting':
            date=[]
            for i in datefinder.find_dates(text):
                date.append(i)

            try:
                MeetingFile.write(blob.noun_phrases[0]+","+str(date[0])+"\n")
                return "meeting saved by the name "+"'"+str(blob.noun_phrases[0])+"'"+" for date "+str(date[0])+". Call me when you need it, or type 'when are my meetings' "
            except IndexError:
                MeetingFile.write(text+","+str(date[0])+"\n")
                return "Could not generate a Title. Saved as "+"'"+text+"'"+"for date "+str(date[0])+". Call me when you need it, or type 'when are my meetings' "


        elif classifier.classify(text)=="google" :
            try:
                if len(blob.noun_phrases[0].split())>1:
                    webbrowser.open("https://www.google.co.in/#q="+blob.noun_phrases[0])
                else:
                    webbrowser.open("https://www.google.co.in/#q=" + text)
            except IndexError:
                webbrowser.open("https://www.google.co.in/#q="+text)

            return "I opened your web browser, It might take some time to open. You can see your answer there."

        elif classifier.classify(text)=="hi":
            return "hi"
        elif classifier.classify(text) == "transalate":

            answer=""
            Textlanguage=blob.detect_language()
            answer=str(blob.translate(from_lang=Textlanguage,to="en"))
            print(Textlanguage)
            x=answer.split()
            print(x)
            x.remove('to')
            x.remove('Translate')
            x.remove('english')
            print(x)
            answer=""
            for i in x:
                answer+=i
                answer+=" "
            print(str(x))
            lang=""
            lang_df=lang_df.set(["ISO"])
            x = df.loc[Textlanguage].to_string().split()
            x.remove("Full")
            lang=x.join()

            return str(answer+" original language was "+lang)


        elif classifier.classify(text)=="bye":
            return "bye"
        elif classifier.classify(text)=="you_are_welcome":
            return "you are welcome"
        else:
            return "I am sorry, but This functionality may be only at the desktop app"
