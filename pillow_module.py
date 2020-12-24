from PIL import Image
# u.png
# 1.jpg
img = Image.open("u.png")

# img.show()


print(img.height)#768

print(img.width)#1366

print(img.size) #(1366,768) (width,height)

print(img.format) #PNG


size = (600,600)
img.thumbnail((size))
img.show()

