# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
 
# #creating a new chatbot
# chatbot = ChatBot('Edureka')
# trainer = ListTrainer(chatbot)
# trainer.train([ 'hi, can I help you find a course', 'sure I d love to find you a course', 'your course have been selected'])
 
# #getting a response from the chatbot
# response = chatbot.get_response("I want a course")
# print(response)

# Importing chatterbot
from chatterbot import ChatBot

# Create object of ChatBot class
bot = ChatBot('Buddy')

# Inport ListTrainer
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

from numpy import loadtxt

# f=open('dialogs.txt', 'r')   #.readlines()
# lines = f.

# data = [i.strip('\n').split('\t') for i in open('dialogs.txt')]

data = []
with open("dialogs.txt") as dialog:
    for line in dialog:
        fields = line.split("\t")
        data.append(fields[0])
        #data.append(fields[1])


trainer.train(data)


name=input("Enter Your Name: ")

print("Welcome to the Bot Service! Let s start a conversation")
while True:
    request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Bot: Bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot:',response)