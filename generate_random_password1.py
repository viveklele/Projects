from random import shuffle, choice
def random_password():   
    special_char1 = ''' !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ '''        
    special_char2 = ''' !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ '''

    upper_case1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    upper_case2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case1 = "abcdefghijklmnopwrstuvwxyz"
    lower_case2 = "abcdefghijklmnopwrstuvwxyz"
    num1 = "1234567890"
    num2 = "1234567890"
    
    
    list1 = [ upper_case1]
    list2 = [special_char1, special_char2, num1, num2 ,upper_case2, lower_case1, lower_case2]
    shuffle(list1)
    shuffle(list2)
    password="" 
    for i in list1:
       temp_pass = (choice(i))
       password = password + temp_pass[0]
    for i in list2:
       temp_pass = (choice(i))
       password = password + temp_pass[0]

    print('Password is: ', password)
random_password()