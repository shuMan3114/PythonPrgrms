import math


number = input("enter a number(>0)")
num_duplicate = int(number)
number_of_digits = math.floor(math.log10(num_duplicate)) +1 
sum = 0
for i in range(0,number_of_digits):
    x = (num_duplicate%10)**number_of_digits
    num_duplicate //= 10
    sum += x

if(sum == int(number)):
    print("armstrong")
else:
    print("not armstrong")
