import random
import pyttsx3
import speech_recognition as sr
import webbrowser 
import datetime
import pyjokes
import pyaudio
import os
import time


# Speech to text
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio, language='en')
            print(data)
            return data
        except sr.UnknownValueError:
            print("Say that again please...")
            

# text to speech
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
   
    if "hello jarvis" in sptext().lower():
        while True:
            data1 = sptext().lower()
            
            if 'your name' in data1:
                name = 'My name is Jarvis'
                speechtx(name)  
                
            elif 'who' in data1:
                who = 'I am your virtual assistant, Jarvis'
                speechtx(who)
                
            elif 'old are you'in data1:
                age = f'I am {random.randint(1,100)} year old'
                speechtx(age)
                
            elif 'time' in data1:
                time = datetime.datetime.now().strftime('%I:%M %p')
                speechtx(time)
                
            elif 'date' in data1:
                date = datetime.datetime.now().strftime('%d:%B:%Y')
                speechtx(date)
                
            elif 'youtube' in data1:
                webbrowser.open('https://www.youtube.com/')
                
            elif 'google' in data1:
                webbrowser.open('https://www.google.com/')
                
            elif 'joke' in data1:
                joke = pyjokes.get_joke(language='en', category='neutral')
                print(joke)
                speechtx(joke)
                
            elif 'instagram' in data1:
                webbrowser.open('https://www.instagram.com/')
                
            elif 'facebook' in data1:
                webbrowser.open('https://www.facebook.com/')
                
            elif 'play song' in data1:
                address = "D:/music"    # give the path in your pc for the song
                listsong = os.listdir(address)
                #print(listsong)
                os.startfile(os.path.join(address, listsong[random.randint(0, 11)]))
                # os.startfile(os.path.join(address, listsong[0]))           # [0] is for the 0th index as in first song in the list
                
            elif 'exit' in data1:
                speechtx('Thanks for using me')
                break
            
            time.sleep(10)
            
    else:
        speechtx('Thanks for using me')
        print("Thanks for using me")