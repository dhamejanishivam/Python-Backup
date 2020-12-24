def pass123():

    import random
    import array

    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    new_list = DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACTERS

    r_digit = random.choice(DIGITS)
    r_low = random.choice(LOCASE_CHARACTERS)
    r_up = random.choice(UPCASE_CHARACTERS)

    pass1 = random.choice(new_list)

    r_digit1 = random.choice(DIGITS)
    r_low1 = random.choice(LOCASE_CHARACTERS)
    r_up1 = random.choice(UPCASE_CHARACTERS)


    final_pass = r_digit + r_low + r_up + pass1 + r_digit1 + r_low1 + r_up1
    print(final_pass)


if __name__ == '__main__':

    pass123()