
#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
import pyttsx3
import textblob
from textblob.classifiers import NaiveBayesClassifier
import os
# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

working_dir=os.getcwd()
with open(working_dir+'/train.csv', 'r') as train:
     classifier = NaiveBayesClassifier(train, format="csv")

# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    a=classifier.classify(r.recognize_google(audio))
    engine=pyttsx3.init()
    engine.setProperty("voice", "english-us")
    engine.setProperty("speed","0.01")
    engine.say(a)
    engine.runAndWait()        
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
