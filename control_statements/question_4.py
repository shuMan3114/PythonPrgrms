number = eval(input("enter a number"))

c = 0
for i in range(2,number):
    if(number%i == 0):
        c +=1
if(c):
    print("not a prime")
else:
    print("prime")