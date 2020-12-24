import math
a = float(input("Enter First Number \n"))
b = float(input("Enter Second Number \n"))
c = float(input("Enter Third Number \n"))
def root_calculator(a,b,c):
    def root_1(a,b,c):
        root_1_step_1 = 0
        if ((b**2)-(4**c))>=0:
            root_1_step_1 = math.sqrt((b**2)-(4**c))
            root_1_step_2 = -b+root_1_step_1
            root_1_step_3 = root_1_step_2/(2*a)
            Root_1 = root_1_step_3
            print(f'First Root is {Root_1}')
        else:
            print("Imaginary Roots")
    def root_2(a,b,c):
        root_2_step_1 =0
        if ((b**2)-(4**c))>=0:
            root_2_step_1 = math.sqrt((b**2)-(4**c))
            root_2_step_2 = -b - root_2_step_1
            root_2_step_3 = root_2_step_2 / (2 * a)
            Root_2 = root_2_step_3
            print(f'Second root is  {Root_2}')
        else:
            print("Imaginary Roots")
    root_1(a,b,c)
    root_2(a,b,c)
root_calculator(a,b,c)