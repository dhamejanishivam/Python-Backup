import random as rd



def signup_info():

    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                    'z']
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']

    username = rd.choice(LOCASE_CHARACTERS)+rd.choice(DIGITS)+"_"+rd.choice(DIGITS)+rd.choice(LOCASE_CHARACTERS)+"_"+rd.choice(DIGITS)+rd.choice(LOCASE_CHARACTERS)
    
    password =  rd.choice(LOCASE_CHARACTERS)+rd.choice(DIGITS)+"_"+rd.choice(DIGITS) + "Iloveyou_" +rd.choice(LOCASE_CHARACTERS)+rd.choice(DIGITS)+"_"+rd.choice(DIGITS)

    name = rd.choice(UPCASE_CHARACTERS)+rd.choice(LOCASE_CHARACTERS)+rd.choice(LOCASE_CHARACTERS)+rd.choice(LOCASE_CHARACTERS)+rd.choice(LOCASE_CHARACTERS)

    lastname = rd.choice(UPCASE_CHARACTERS)+rd.choice(LOCASE_CHARACTERS)+rd.choice(LOCASE_CHARACTERS)+rd.choice(LOCASE_CHARACTERS)+rd.choice(LOCASE_CHARACTERS)+rd.choice(LOCASE_CHARACTERS)+rd.choice(LOCASE_CHARACTERS)+rd.choice(LOCASE_CHARACTERS)+rd.choice(LOCASE_CHARACTERS)


    return name , lastname , username , password

if __name__ == "__main__":
    
    print(signup_info())
