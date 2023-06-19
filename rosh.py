import speech_recognition as sr
import pyttsx3
import time
from time import ctime
import webbrowser
import playsound
import os
import random
from gtts import gTTS
from tkinter import *
from PIL import ImageTk,Image

print('Say something...')
r = sr.Recognizer()
speaker = pyttsx3.init()

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

                img = ImageTk.PhotoImage(Image.open('chat.png'))
                panel = Label(root, image=img)
                panel.pack(side='right', fill='both', expand='no')
                
                compText = StringVar()
                userText = StringVar()
                
                userText.set('Natasha Your Virtual Assistant')
                userFrame = LabelFrame(root, text='Natasha',bg='#fbbbb9', fg='white', font=('Railways', 24,'bold'))
                userFrame.pack(fill='both', expand='yes')
                
                top = Message(userFrame, textvariable=userText, bg='#fbbbb9',fg='white')
                top.config(font=("Century Gothic", 15, 'bold'))
                top.pack(side='top', fill='both', expand='yes')

# compFrame = LabelFrame(root, text="Natasha", font=('Railways',10, 'bold'))
# compFrame.pack(fill="both", expand='yes')

                btn = Button(root, text='Speak', font=('railways', 10, 'bold'),bg='#fbbbb9', fg='black', command=self.clicked).pack(fill='x',expand='no')
                btn1 = Button(root, text='Chat', font=('railways', 10, 'bold'),bg='#fbbbb9', fg='black', command=self.chat).pack(fill='x',expand='no')
                btn2 = Button(root, text='Close', font=('railways', 10,'bold'), bg='#fbbbb9', fg='black', command=root.destroy).pack(fill='x', expand='no')
                
##                nat_voice('How can i help you?')
                root.mainloop()
        def chat(self):
                pass
        def clicked(self):#BUTTON CALLING
                print("working...")
                voice_data = record_audio()
                voice_data = voice_data.lower()
                if 'who are you' in voice_data:
                        nat_voice('My name is Natasha ')
                if 'search' in voice_data:
                        search = record_audio('What do you want to search?')
                        if search is not None:
                                url = 'https://google.com/search?q=' + search
                                webbrowser.get().open(url)
                                nat_voice('Here is what i found on google for ' + search)
                        else:
                                record_audio("Try Again")
                if 'find location' in voice_data:
                        location = record_audio('What is your location?')
                        url = 'https://google.nl/maps/place/' + location + '/&amp;'
                        webbrowser.get().open(url)
                        nat_voice('Here is ' + location)
                if 'what is the time' in voice_data:
                        nat_voice("The time is :" + ctime())
                if 'bye' in voice_data:
                        nat_voice('Ba-Bye, have a good day. ')
                        root.destroy()
                        exit()


if __name__== '__main__':
        widget = Widget()

time.sleep(100)
while 1:
        voice_data = record_audio()
        respond(voice_data)

speaker.runAndWait()


#CHATBOT
