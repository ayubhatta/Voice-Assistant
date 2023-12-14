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
        recognizer.adjust_for_ambient_noise(source)                        # adjust the energy threshold based on the surrounding noise level
        audio = recognizer.listen(source)                                  # listens to the audio from the microphone
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio, language='en')       # language='en' for english language
            print(data)
            return data
        except sr.UnknownValueError:
            print("Say that again please...")
            

# text to speech
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)        # [0]th index for male voice and [1] index for female voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)                  # 150 words per minute
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
   
   # Giving Commands 
    if "hello jarvis" in sptext().lower():
        while True:
            print('How can I help you?')
            speechtx('How can I help you?')
            data1 = sptext().lower()
            
            if 'your name' in data1:                                    # use keyword 'your name' to ask the name of the assistant
                name = 'My name is Jarvis'       
                print(name)
                speechtx(name)  
                
            elif 'who' in data1:                                        # use keyword 'who' to ask who the assistant is
                who = 'I am your virtual assistant, Jarvis'
                print(who)
                speechtx(who)
                
            elif 'old are you'in data1:                                 # use keyword 'old are you' to ask the age of the assistant
                age = f'I am {random.randint(1,100)} year old'          # It generates random age from 1 to 100
                print(age)
                speechtx(age)
                
            elif 'time' in data1:                                       # use keyword 'time' to ask the time
                time = datetime.datetime.now().strftime('%I:%M %p')
                print(time)
                speechtx(time)
                
            elif 'date' in data1:                                       # use keyword 'date' to ask the date
                date = datetime.datetime.now().strftime('%d:%B:%Y')
                print(date)
                speechtx(date)
                
            elif 'youtube' in data1:                                    # use keyword 'youtube' to open youtube
                webbrowser.open('https://www.youtube.com/')
                
            elif 'google' in data1:                                     # use keyword 'google' to open google
                webbrowser.open('https://www.google.com/')
                
            elif 'joke' in data1:                                       # use keyword 'joke' to ask for a joke
                joke = pyjokes.get_joke(language='en', category='neutral')
                print(joke)
                speechtx(joke)
                
            elif 'instagram' in data1:                                  # use keyword 'instagram' to open instagram                                           
                webbrowser.open('https://www.instagram.com/')
                
            elif 'facebook' in data1:                                   # use keyword 'facebook' to open facebook                          
                webbrowser.open('https://www.facebook.com/')
                
                
            # only if you want to play the song from your pc
            elif 'play song' in data1:                                   # use keyword 'play song' to play a song from your pc
                address = "D:/music"    # give the path of the folder in your pc for the song
                listsong = os.listdir(address)
                #print(listsong)
                os.startfile(os.path.join(address, listsong[random.randint(0, 11)]))
                # os.startfile(os.path.join(address, listsong[0]))       # [0] is for the 0th index as in first song in the list
                
            elif 'exit' in data1:                                        # use keyword 'exit' to exit the program
                speechtx('Thanks for using me')
                print('Thanks for using me')
                break
            
            time.sleep(10)         # This command is used to give a break of 10 seconds after each command
            
    else:
        print("Thanks for using me")     # Prints this if the keyword 'hello jarvis' is not used
        speechtx('Thanks for using me')  # Speaks this if the keyword 'hello jarvis' is not used
        
