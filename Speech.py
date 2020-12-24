import random 
import time 
import speech_recognition as sr 
import pyttsx3 
from win32com.client import Dispatch 
from datetime import datetime 
from datetime import date 
import sys
import os
from selenium import webdriver
import wikipedia as wiki
from pytube import YouTube

# Another projects -  
import gui_music_player
import notepad
import email_sender

 
recognizer = sr.Recognizer() 
microphone = sr.Microphone() 
clear = os.system('cls')
email_reciver = ['shivam','mohit']

def time_teller():
    now = datetime.now() 
    hour = now.strftime("%H") 
    minute = now.strftime("%M") 
    realtime = now.strftime("%H:%M:%S") 
    hour = int(hour) 
    minute = int(minute) 
    say(f'Time is {hour} hours and {minute} minutes ')

def say(string): 
    speak = Dispatch("SAPI.SpVoice") 
    speak.Speak(string) 

def voice_input(recognizer, microphone): 
    with microphone as source: 
        recognizer.adjust_for_ambient_noise(source) 
        print("Listening...") 
        audio = recognizer.listen(source) 
    # try recognizing the speech in the recording 
    # if a RequestError or UnknownValueError exception is caught, 
    #     update the response object accordingly 
    new_text = ""
    try: 
        text = recognizer.recognize_google(audio)
        for letters in text:
            new_text = new_text + letters.lower()
    except sr.RequestError: 
        # API was unreachable or unresponsive 
        text = "API Unavialabel" 
        new_text = "API Unavialabel" 
    except sr.UnknownValueError: 
        # speech was unintelligible 
        text = "Unable to recognize speech" 
        new_text = "Unable to recognize speech" 
    print(new_text)
    return new_text 

def time_gretting(): 

    now = datetime.now() 
    hour = now.strftime("%H") 
    minute = now.strftime("%M") 
    realtime = now.strftime("%H:%M:%S") 
    hour = int(hour) 
    minute = int(minute) 
    final = "Empty" 

    # Time section - 

    if hour>=23 and minute>=30 :
        say(f'Good evening boss it is {hour} {minute} in night ')
        time.sleep(0.3)
        say(f'Boss it is too late in night , do you want me to proceed ')
        vi = voice_input(recognizer,microphone)
        if vi=="yes" or vi=="Yes" :
            say("As you wish boss")
            return ""
        elif vi=="no" or vi=="No" :
            say("It is good for you boss")
            sys.exit()
        else :
            pass
    
    if hour>=23 and minute<30 and minute>=10 :
        say(f'Good evening boss it is {hour} {minute} in night ')
    
    if hour>=23 and minute<30 and minute<10 :
        say(f'Good evening boss it is {hour} o {minute} in night ')
    
    if 23>hour>=21 :
        say(f'Good evening boss it is {hour}  {minute} in night')

    if 21>hour>=16 :
        say(f'Good evening boss it is {hour}  {minute} in evening ')

    if 16>hour>=12 :
        say(f'Good afternoon boss it is {hour} {minute} in afternoon ') 

    if 12>hour>=4 :
        say(f'Good morning boss ')
        time.sleep(0.3)
        say(f'it is {hour} {minute} in morning ')

    if 4>hour>=0 :
        say(f'Boss it is too early in morning , do you want me to proceed ')
        vi = voice_input(recognizer,microphone)
        if vi=="yes" or vi=="Yes" :
            say("As you wish boss")
            return ""
        elif vi=="no" or vi=="No" :
            say("It is good for you boss")
            sys.exit()
        else:
            pass

def condition_checker():

    vi = voice_input(recognizer,microphone)
    for letters in vi :
        letters = letters.lower()

    if vi=="time" or vi=="Time" or vi=="tell me the time" or vi=="what time it is" :
        time_teller()
    
    elif vi=="song" or vi=="Song" or vi=="Play song" or vi=="Play Song" or vi=="play song" or vi=="play some songs" or vi=="open music player" :
        say("Opening music player")
        gui_music_player.music_play()
        

    elif vi=="hey" or vi=="hi" or vi=="hello" :
        to_greet = random.choice("hey","hi") 
        say(f'{to_greet}')

    elif vi=="notepad" or vi=="open notepad" or vi=="open Notepad" :
        say("Opening notepad ")
        notepad.notepad_main()
    
    elif vi=="open youtube" :
        site = webdriver.Chrome()
        site.maximize_window()
        site.get('https://www.youtube.com/')
    
    elif vi=="send email" or vi=="i want to send a email" or vi=="i want to send an email" or vi=="send an email" :
        sender_email = "dhamejanimain@gmail.com"
        password = "Iloveyou_3000"
        # reciver_email = "dhamejanishivam@gmail.com"
        say('Boss email will be sent from your registered email')
        time.sleep(0.2)
        say("Is it ok ")
        vi = voice_input(recognizer,microphone)
        if vi=="yes" or vi=="ok" or vi=="yeah" or vi=="absoluetly" or vi=="perhaps yes" or "yes" in vi :
            say('Your registered email reciver name are -')
            for item in email_reciver :
                say(item)
            say("whom should I send email")
            vi = voice_input(recognizer,microphone)
            if vi=="shivam" :
                reciver_email = "dhamejanishivam@gmail.com"
            elif vi=="mohit" :
                reciver_email = "mohitdhamejani2000@gmail.com"
            else:
                say('Sorry I was not able to understand that ')
                return ""
            say('What should I write in Email ')
            vi = voice_input(recognizer,microphone)
            message = str(vi)
            try:
                password = "Iloveyou_3000"
                email_sender.email_function(sender_email=sender_email,reciver_email=reciver_email,your_password=password,message=message)
                say("the email has been sent sucessfully")
            except Exception as e :
                print(e)
                say("I am having some trouble sending the email please try after some time")
        
        else:
            say("Ok ")
            return None
    
    elif  "wikipedia" in vi or "wikipidia" in vi   :
        try :
            result = wiki.summary(vi,sentences=3)
            say("Let me check it on internet")
            say(result)
        except Exception as e :
            say("Sorry boss I am not able to serch")
    
    elif vi=="open site" or vi=="open a site" or vi=="site" :
        pass

    elif vi=="search in google" or "search in google" in vi or "google search" in vi:
        say("What do you want to search ")
        vi = voice_input(recognizer,microphone)
        b = vi.split(' ')
        new_str = ''
        count = 0
        for i in b :
            new_str += str(i) 
            if count<(len(b)-1) :
                new_str+="+"
            count+=1
        site = webdriver.Chrome()
        site.maximize_window()
        site.get(f'https://www.google.com/search?q={new_str}')
        while True :
            if site.close() == True :
                break
            else :
                continue
    
    
    elif vi=="download youtube video" or "video download" in vi :
        say("Please paste the url in terminal")
        url = input() 
        try :
            yt = YouTube(url)
            select = yt.streams.filter(progrssive=True,file_extension='mp4').last()
            select.download("D:\\")

        except Exception as e :
            say("eror")
            print(e)

    else:
        say(f'I am sorry I didnot get that ')
        time.sleep(0.3)
        say('You can ask something like')
        time.sleep(0.1)
        say("tell me the time")
        say("play some songs")


def task_listner():
    task_list = ("\nThings you can ask me to do - \n"
                f'Play some songs for playing song \n'
                f'Open notepad to open notepad \n'
                f'Send an email to send email \n'
                f'Open youtube to open youtube \n'
                f'Open site to open any site \n'

    "\n")
    clear
    print(task_list)
    for i in range(1):
        condition_checker()    
    say("Do you want me to do anything else")
    vi = voice_input(recognizer,microphone)
    if vi=='yes'or vi=="Yes" :
        say('What else I can do  for you boss ')
        task_listner()
    elif vi=="no" or vi=="No" or vi=="goodbye" :
        say("Ok goodbye ")
        time.sleep(0.2)
        say("have a great day")
        clear
        sys.exit()
    elif vi=="no thank you" or vi=="no thankyou":
        say("it is pleasure working with you boss")
    else:
        say("Do you want me to do anything else")
        vi = voice_input(recognizer,microphone)
        if vi=='yes'or vi=="Yes" :
            say('What else I can do  for you boss ')
            task_listner()
        elif vi=="no" or vi=="No" :
            say("Ok goodbye ")
            time.sleep(0.2)
            say("have a great day")
            clear
            sys.exit()
        else:
            say('Ok goodbye')
            clear
        


if __name__ == "__main__": 
    
    time_gretting()
    say("What can I do for you ")
    task_listner()
        

        
     

 
 
 

 