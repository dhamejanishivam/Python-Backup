import pyttsx3
import speech_recognition as sr
import pyaudio
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def tc():
    r = sr.Recognizer()
    # r.energy_threshold = 1
    with sr.Microphone() as source :
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    # try :
    # print("Recognising...")
    query = r.recognize_google(audio)
    query = query.lower()
    # time.sleep(1)
    speak(query)
    print(query)
    # except Exception as e :
    #     print(e)

# speak("Harry")
# print("Hello")
# while(True):
tc()


