from errno import ESTALE


number = eval(input("Enter a number"))

if(number):
    if(number > 0):
        print("+ve")
    else:
        print("-ve")
else:
    print("zero")
