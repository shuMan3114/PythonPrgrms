year = eval(input("Enter a year: "))

if(year%4 == 0):
    if(year%400 == 0):
        print("leap year")
    else:
        if(year%100 == 0):
            print("not leap year")
        else:
            print("leap year")
else:
    print("not a leap year")