upper = 10

#print("Prime numbers between", lower, "and", upper, "are:")

for num in range(2, upper):
   #print('forloopnum = ', num)
   # all prime numbers are greater than 1
   #if num > 1:
    for i in range(2, num): # num = 6
        if (num % i) == 0:  # i=2 
            break
    else:
        print('prime num is = ', num)
        