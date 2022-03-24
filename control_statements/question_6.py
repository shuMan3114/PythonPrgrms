import math


prompt = "enter AC{area for circle} AR{area for rectangle} CC{circumfrence of circle} AS{area of square}"
verdict = input(prompt).lower()

if(verdict == 'ac'):
    radius = eval(input("enter radius: "))
    area = math.pi*(radius**2)
    print(area)
elif(verdict == 'ar'):
    length = eval(input("enter length"))
    breadth = eval(input('enter breadth0'))
    area = length*breadth
    print(area)
elif(verdict == 'cc'):
    radius = eval(input("enter radius: "))
    circumfrence = math.pi*(radius*2)
    print(circumfrence)
elif(verdict == 'as'):
    side = eval(input("enter side: "))
    area = side**2
    print(area)
else:
    print("invalid")