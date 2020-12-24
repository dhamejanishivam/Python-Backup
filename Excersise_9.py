from win32com.client import Dispatch
import requests as re

def ai(str):
    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)



news_1 = re.get("http://newsapi.org/v2/everything?q=bitcoin&from=2020-09-30&sortBy=publishedAt&apiKey=d833f88cefb14f4d8845190056c17723")
news_1_p = news_1.text
ai(news_1_p)
