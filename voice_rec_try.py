import speech_recognition as sr

r = sr.Recognizer()


with sr.Microphone() as source :
    audio_text = r.listen(source)
with sr.Microphone() as source:
    audio_text = r.listen(source)

    text = r.recognize_google(audio_text, language='en')
    f = open("rec.txt" , "a")
    f.write("\n")
    f.write(text)
    f.write("\n")
    f.close()

