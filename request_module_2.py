import requests
from PIL import Image

# r = requests.get("https://xkcd.com/353/")
# print(r) # It shows response of website
# print(dir(r)) # It show all attribute 
# print(help(r)) # It show atrribute and its funtions
# print(r.text)



# Below Code get image url , save it in bite form in file and open it - 
"""image_url = requests.get(' https://imgs.xkcd.com/comics/python.png')
ab = open ("request_module_image_byte.png" , "wb")
ab.write(image_url.content)
c = "request_module_image_byte.png"
image = Image.open(c)
image.show()"""
# Code ends here.


# r = requests.get('https://imgs.xkcd.com/comics/python.png')
# print(r.status_code) 
# print(r.ok) # If site is accesible for all it will print true else: false
# print(r.headers)


r = requests.get('https://httpbin.org/get')
print(r)
