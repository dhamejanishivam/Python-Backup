import os


# D:\Other\practice

print("Enter path \n"
      "D:\Other\practice \n"
      "")
f = input()
def ren(f):
    os.chdir("C:\\Users\Lenovo\PycharmProjects\pythonProject3\\venv")
    a = open("file.txt")
    b = [a.read()]
    for d in b :
        pass
    os.chdir(f"{f}")
    e = (os.listdir())
    for item in e :
        if item!=d :
            z = item
            # if os.path.isfile(z):
                   # os.rename(z , z.capitalize())
            # else: pass
        elif item==d:
            pass
        else: break

    g = (os.listdir())
    h = []
    for items in g :
        # print(items)
        items = items.split(".")
        h.append(items)
    print(h)
    for j in h :
        if j=="txt"  :
            print("yes " , j)
        else: print("n")


ren(f)