import speech_recognition as sr
import pyttsx3
import time
from time import ctime
import webbrowser
import playsound
import os
import random
from gtts import gTTS
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

print('Say something...')
r = sr.Recognizer()
speaker = pyttsx3.init()

global flag
global questionField
global textarea
flag = 0

file = "new_chat.txt"
bot=ChatBot('Bot')
trainer=ListTrainer(bot)
trainer.train(file)

def record_audio(ask = False):
#user voice record
        with sr.Microphone() as source:
                if ask:
                        nat_voice(ask)
                audio = r.listen(source)
                voice_data = ''
        try:
                voice_data = r.recognize_google(audio)
                print('Recognizer voice :'+ voice_data)

        except Exception:
                print('Oops something went Wrong')
                nat_voice('Oops something went Wrong')
                return None
        return voice_data

def nat_voice(audio_string):
        #Play audio text to voice
        tts = gTTS(text=audio_string, lang='en')
        r = random.randint(1, 10000000)
        audio_file = 'audio-' + str(r) + '.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(audio_string)
        os.remove(audio_file)

class Widget: #GUI OF VIRTUAL ASSISTAND AND COMMANDS GIVEN
        def __init__(self):
                global root
                root = Tk()
                root.title('Natasha')
                root.geometry('720x360')

                global panel
                img = ImageTk.PhotoImage(Image.open('chat.png'))
                panel = Label(root, image=img, width=400)
                panel.pack(side='right', fill='both', expand='no')
                compText = StringVar()
                userText = StringVar()

                userText.set('Natasha Your Virtual Assistant')
                global userFrame
                userFrame = LabelFrame(root, text='Natasha',bg='#fbbbb9', fg='white', font=('Railways', 24,'bold'))
                userFrame.pack(fill='both', expand='yes')

                global top
                top = Message(userFrame, textvariable=userText, bg='#fbbbb9',fg='white')
                top.config(font=("Century Gothic", 15, 'bold'))
                top.pack(side='top', fill='both', expand='yes')
                
                global btn
                global btn1
                global btn2
                btn = Button(root, text='Speak', font=('railways', 10, 'bold'),bg='#fbbbb9', fg='black', command=self.clicked).pack(fill='x',expand='no')
                btn1 = Button(root, text='Chat', font=('railways', 10, 'bold'),bg='#fbbbb9', fg='black', command=self.chat).pack(fill='x',expand='no')
                btn2 = Button(root, text='Close', font=('railways', 10,'bold'), bg='#fbbbb9', fg='black', command=root.destroy).pack(fill='x', expand='no')

                nat_voice('How can i help you?')
                root.mainloop()
                flag = 1 

        def main_page(self):
                self.clear_main()
                compText = StringVar()
                userText = StringVar()

                userText.set('Natasha Your Virtual Assistant')
                global userFrame
                userFrame = LabelFrame(root, text='Natasha',bg='#fbbbb9', fg='white', font=('Railways', 24,'bold'))
                userFrame.pack(fill='both', expand='yes')

                global top
                top = Message(userFrame, textvariable=userText, bg='#fbbbb9',fg='white')
                top.config(font=("Century Gothic", 15, 'bold'))
                top.pack(side='top', fill='both', expand='yes')

                global btn
                global btn1
                global btn2
                btn = Button(root, text='Speak', font=('railways', 10, 'bold'),bg='#fbbbb9', fg='black', command=self.clicked).pack(fill='x',expand='no')
                btn1 = Button(root, text='Chat', font=('railways', 10, 'bold'),bg='#fbbbb9', fg='black', command=self.chat).pack(fill='x',expand='no')
                btn2 = Button(root, text='Close', font=('railways', 10,'bold'), bg='#fbbbb9', fg='black', command=root.destroy).pack(fill='x', expand='no')

                nat_voice('How can i help you?')
                root.mainloop()
                flag = 1
                
        def botReply(self):
                print("I'm in.")
                global questionField
                question=questionField.get()
                question=question.capitalize()
                print(question)
                answer=bot.get_response(question)
                global textarea
                textarea.insert(END,'You: '+question+'\n\n')
                textarea.insert(END,'Bot: '+str(answer)+'\n\n')
                pyttsx3.speak(answer)
                questionField.delete(0,END)

        def clear_main(self):
                for i in range(len(root.winfo_children())-1):
                        print(i)
                        root.winfo_children()[1].destroy()
        def chat(self):
                flag = 0
                self.clear_main()
                centerFrame=Frame(root)
                centerFrame.pack()

                scrollbar=Scrollbar(centerFrame)
                scrollbar.pack(side=RIGHT, fill='y')

                global textarea
                textarea=Text(centerFrame, font=('times new roman', 16, 'bold'), height='7.5px', yscrollcommand=scrollbar.set, wrap='word')
                textarea.pack(pady='2px', side='left')
                scrollbar.config(command=textarea.yview)

                Label(root, text='Enter your message here', font=('times new roman', 8, 'bold'), bg='#fbbbb9', fg='black').pack(fill='both')

                global questionField
                questionField=Entry(root, font=('times new roman', 20))
                questionField.pack(pady='2px', fill='both')

                submitButton=Button(root, text='Submit', command=lambda:self.botReply(), font=('railways', 10, 'bold'), bg='#fbbbb9', fg='black')
                submitButton.pack(fill='x', expand='no')
                back=tk.Button(root, text='Back', command=lambda:self.main_page(), font=('railways', 10, 'bold'), bg='#fbbbb9', fg='black')
                back.pack(fill='x', expand='no')

        def clicked(self):#BUTTON CALLING
                print("working...")
                voice_data = record_audio()
                voice_data = voice_data.lower()
                if 'hello' in voice_data or 'hi' in voice_data:
                        nat_voice('hi, there')
                if 'who are you' in voice_data or 'name' in voice_data:
                        nat_voice('My name is Natasha ')
                if 'search' in voice_data:
                        search = record_audio('What do you want to search?')
                        if search is not None:
                                url = 'https://google.com/search?q=' + search
                                webbrowser.get().open(url)
                                nat_voice('Here is what i found on google for ' + search)
                        else:
                                record_audio("Try Again")
                if 'location' in voice_data:
                        location = record_audio('What\'s the location to find?')
                        url = 'https://google.nl/maps/place/' + location + '/&amp;'
                        webbrowser.get().open(url)
                        nat_voice('Here is ' + location)
                if 'what is the time' in voice_data:
                        nat_voice("The time is :" + ctime()[11:19])
                if 'bye' in voice_data:
                        nat_voice('Ba-Bye, have a good day. ')
                        root.destroy()
                        exit()


if __name__== '__main__':
        widget = Widget()

time.sleep(100)
while flag == 1:
        voice_data = record_audio()
        respond(voice_data)

speaker.runAndWait()
