from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3

##data_list=[ 'What is the capital of India',
##            'Delhi is the capital of India',
##            'In which language you talk',
##            'I mostly talk in english',
##            'What you do in free time',
##            'I memorize things in my free time',
##            'Ok bye',
##            'bye take care'
##
##            ]
##
##bot=ChatBot('Bot')
##trainer=ListTrainer(bot)
##
### for files in os.listdir('data/french/'):
###     data=open('data/french/'+files,'r',encoding='utf-8').readlines()
##
##trainer.train(data_list)

def botReply():
    question=questionField.get()
    question=question.capitalize()
    answer=bot.get_response(question)
    textarea.insert(END,'You: '+question+'\n\n')
    textarea.insert(END,'Bot: '+str(answer)+'\n\n')
    pyttsx3.speak(answer)
    questionField.delete(0,END)

root=Tk()

root.geometry('720x360')
root.title('ChatBot created by Shweta and Roma')
root.config(bg='#fbbbb9')

logoPic=PhotoImage(file='chat1.png')

logoPicLabel=Label(root,image=logoPic,bg='#fbbbb9')
logoPicLabel.pack(side='right', fill='both', expand='no')

centerFrame=Frame(root)
centerFrame.pack()

scrollbar=Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT, fill='y')

textarea=Text(centerFrame, font=('times new roman', 16, 'bold'), height='8px', yscrollcommand=scrollbar.set, wrap='word')
textarea.pack(pady='2px', side='left')
scrollbar.config(command=textarea.yview)

Label(root, text='Enter your message here', font=('times new roman', 8, 'bold'), bg='#fbbbb9', fg='white').pack(fill='both')

questionField=Entry(root, font=('times new roman', 20))
questionField.pack(pady='2px', fill='both')

submitButton=Button(root, text='Submit', command=botReply, font=('railways', 10, 'bold'), bg='#fbbbb9', fg='white')
submitButton.pack(fill='x', expand='no')

def click(event):
    submitButton.invoke()

root.bind('<Return>',click)

root.mainloop()
