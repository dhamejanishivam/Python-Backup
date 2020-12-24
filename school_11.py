"""
Take a string as a input
To print -
Number of uppercase
Number of lowercase
Number of digits
Number of alphabets
"""
a = input("Enter \n")
no_upper = 0
no_lower = 0
no_digit = 0
no_alpha = 0
upper_is_are = "is"
lower_is_are = "is"
digit_is_are = "is"
alpha_is_are = "is"
for item in a:
    if item.isupper():
        no_upper+=1
        no_alpha+=1
    if item.islower():
        no_lower+=1
        no_alpha+=1
    if item.isnumeric():
        no_digit+=1

if no_upper>1:
    upper_is_are = "are"
if no_lower>1:
    lower_is_are = "are"
if no_digit>1:
    digit_is_are = "are"
if no_alpha>1 :
    alpha_is_are = "are"
print(f'The number of upper case {upper_is_are} {no_upper}')
print(f'The number of Lower case {lower_is_are} {no_lower}')
print(f'The number of Digits {digit_is_are} {no_digit}')
print(f'The number of Alphabets {alpha_is_are} {no_alpha}')
