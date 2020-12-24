from time import sleep

def sercher():
    sleep(4)
    book = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 "
    while(True):
        text = (yield)
        if text in book :
            print("y")
        else:
            print("name is not in book")

serch = sercher()
next(serch)
serch.send("shivam")
input()
serch.send("is a")
