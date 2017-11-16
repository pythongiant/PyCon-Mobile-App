#Imnport libraries
from textblob import TextBlob

UserInput=raw_input("Please give your rating:")
UserInText=TextBlob(UserInput)

print (UserInText.sentiment)