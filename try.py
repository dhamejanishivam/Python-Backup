try :
    open("this_file_does_not_exsist")
except Exception as a :
    print(f"Eror =  {a}   \n"
          f"Eror ends here \n")

finally:  # The code inside 'finally' statement will run anyway
    print("This will happen anyway \n"
          "it does not matter that above line was runned or not \n")#

print("Eror does appered , but program still runned till here")
