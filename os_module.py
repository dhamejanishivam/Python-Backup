import  os

# print(os.getcwdb())  # This shows current working folder

# os.chdir('C://') # By this we can change our working foler

# print(os.getcwdb())

# print(os.listdir())  # This function tell name of all file and folder in working folder

# os.mkdir("Folder")  # This function create folder
# os.rmdir("Folder")   # This function delete folder


print(os.listdir())



# os.rename("pyvenv.cfg" , "unknow.cfg") # ( "original_name" , "new_name" )

print(os.path.isdir("c://Program Files"))  # This tell if entered folder is present or not

print(os.path.isfile("c://Program Files"))  # This tell if entered file is present or not