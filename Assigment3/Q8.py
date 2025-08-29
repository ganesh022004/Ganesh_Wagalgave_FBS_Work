import random

username = input("Enter user name: ")
if username == 'ganesh':
    # Captcha generate
    Captcha = random.randint(1000, 9999)
    print("Captcha is:", Captcha)
    
    user_input = input("Enter Captcha: ")

    # Captcha check
    if user_input == str(Captcha):
        print("Captcha is correct")
    else:
        print("Captcha is wrong")
else:
    print("Username is not correct")
