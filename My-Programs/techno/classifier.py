import textblob
from textblob.classifiers import NaiveBayesClassifier


working_dir=os.getcwd()
with open(working_dir+'/train.csv', 'r') as train:
     classifier = NaiveBayesClassifier(train, format="csv")
