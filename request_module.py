import  requests

r = requests.get("https://www.youtube.com/watch?v=JFm7YDVlqnI&list=RDMMJFm7YDVlqnI&start_radio=1")
print(r.text)  # By this we can read html content

url = "www.something.com"

data  = {
    "p1" : 4
    "p2" : 8
}
r2 = requests.post(url=url , data=data)