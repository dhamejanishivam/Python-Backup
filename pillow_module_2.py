from PIL import Image

image = Image.open("u.png")
# new_i = image.rotate(90) 
# new_i.show()
# image.show()

crop_cor = (0,0,500,500)
crop_i = image.crop(crop_cor).show()  # (x,y) (x1,y1)





