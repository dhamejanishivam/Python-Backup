# Name genrator code starts here -


import random

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

symbols = ['_']


r_low = random.choice(LOCASE_CHARACTERS)
r_up = random.choice(UPCASE_CHARACTERS)
r_low1 = random.choice(LOCASE_CHARACTERS)
r_up1 = random.choice(UPCASE_CHARACTERS)
r_low2 = random.choice(LOCASE_CHARACTERS)
r_low3 = random.choice(LOCASE_CHARACTERS)
r_low4 = random.choice(LOCASE_CHARACTERS)
r_low5 = random.choice(LOCASE_CHARACTERS)
r_low6 = random.choice(LOCASE_CHARACTERS)

name1 =  r_up + r_low + r_low1 + r_low2
name2 = r_up1 + r_low3 + r_low4 + r_low5 + r_low6

print(f"{name1}_{name2} ")


# Name genrator code ends here.