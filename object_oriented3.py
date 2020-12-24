print("\n")
class student :
    def __init__(self, aname, asalary, arole ): # This function automatimaticly assign name to aname and so on.
        self.name = aname
        self.salary = asalary
        self.role = arole

    def pd(a):
        return(f"Name is {a.name} , Standard is {a.std}")

    @classmethod
    def changel(cls , newleaves):
        cls.l = newleaves

    @classmethod
    def from_str(cls , string):
        # params = string.split("-")                        # This two lines are same as third line
        # return cls(params[0] , params[1] , params[2])     #
        return cls(*string.split("-"))  # This is one line function for above two lnes

shivam = student("Shivam" , "45000000", "Head" )
bkl = student("Bhen_ka_lawda" , "Galli ki salray nahi hoti hai" , "Dene ke kaam ati hai")
karan = student.from_str("Karan-480-student")

# print(shivam.__dict__) # This will print all details for name entered

# print(shivam.__dict__)
# shivam.changel(5)
# print(shivam.l)
# student.nof = 10
# print(shivam.nof)

print(karan.salary)



