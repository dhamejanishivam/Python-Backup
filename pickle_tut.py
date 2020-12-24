import pickle
# Pickling is use to store any list,tupple etc to reduce time for obtaing list again.

# Pickling -


# cars = ["Mercedes" , "Bmw" , "Lykan"]
# file = "mycar.pkl"
# fileobj = open(file , "wb")
# pickle.dump(cars , fileobj)
# fileobj.close()




# Unpickling an file -

file = "mycar.pkl"
fileobj = open(file , "rb")
mycar = pickle.load(fileobj)
print(mycar)

mycar = pickle.lo