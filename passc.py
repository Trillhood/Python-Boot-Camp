# Author: Ian Mike 
# Program to generate a random password


import random, string

lower_case = string.ascii_lowercase 
upper_case = string.ascii_uppercase 
numbers = string.digits 
signs = string.punctuation 
def password_picker(lower, upper, numbers, signs):
    random_password = []
    random_password.append(random.sample(lower, 2))
    random_password.append(random.sample(upper, 2))
    random_password.append(random.sample(numbers, 2))
    random_password.append(random.sample(signs, 2))
    final = random.sample(random_password, 4)
    password = ""
    for a in final:
        b = ''.join(map(str, a))
        password = password +  b
    print("Your random password :  ", password)

password_picker(lower_case, upper_case, numbers, signs)


