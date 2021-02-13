import re
def password_verification(password):
    state = 0
    while True:   
        if len(password) <= 8:
            print("Password length then less then 8")
            state = 1
            break
        elif not re.search("[a-z]", password): 
            print("You not entre small characters")
            state = 1
            break
        elif not re.search("[A-Z]", password): 
            print("You not entered capital latter")
            state = 1
            break
        elif not re.search("[0-9]", password): 
            print('You not entered numbers')
            state = 1
            break
        elif not re.search('''[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]''', password): 
            print('You not entered special characters')
            state = 1
            break
        else: 
            print("Valid Password")
            break
      
    if state ==1:
        print("Not a Valid Password")
    
user_input = input('Enter password: ')
password_verification(user_input)