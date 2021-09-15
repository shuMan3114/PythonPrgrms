import math
import operator

# program 1
print("-----------------------------------------------------")
print("program 1")
length = eval(input("Enter number of numbers: "))
smallestNumber = eval(input("Enter number 1: "))
for m in range(2, length + 1):
    inputString = "Enter number " + str(m) + " : "
    numberEntered = eval(input(inputString))
    if numberEntered < smallestNumber:
        smallestNumber = numberEntered
print("Smallest number is:", smallestNumber)

# program 2
print("-----------------------------------------------------")
print("program 2")
# workingHoursDay = eval(input("Enter working hours / day: "))
earningPerDay = eval(input("Enter earnings/ day: "))
earningsPerWeek = earningPerDay * 6
if earningsPerWeek > 4000:
    print("Enter Text here: ")
else:
    print("Do not enter Text here: ")

# program 3
print("-----------------------------------------------------")
print("program 3")
num1 = eval(input("Enter number 1: "))
num2 = eval(input("Enter number 2: "))
if num1 > num2:
    print(num1, "is greater")
elif num2 > num1:
    print(num2, "is greater")
else:
    print("both are equal")

# program 4
print("-----------------------------------------------------")
print("program 4")
number = eval(input("Enter a number"))
if number % 5 == 0:
    print("Number divisible by 5")
else:
    print("Number not divisible by 5")

# program 5
print("-----------------------------------------------------")
print("program 5")
percentageOfStudent = eval(input("Enter percentage: "))
if percentageOfStudent > 85:
    print("Grade is A")
elif 70 < percentageOfStudent <= 85:
    print("Grade is B")
else:
    print("Grade is C")
print("-----------------------------------------------------")

# display a menu for calculating area of circle or perimeter
print("INSTRUCTIONS:" "\n" "For perimeter of circle, enter 1" "\n" "For area of circle, enter 2")
calcToBeDone = eval(input("Enter code for calculation: "))
radius = eval(input("Enter radius of circle: "))
if calcToBeDone == 1:
    perimeter = math.pi * radius * 2
    print("Perimeter is", perimeter)
else:
    area = math.pi * (radius ** 2)
    print("Area is", area)

# if num even square if num odd cube
numberEntered = eval(input("Enter a number: "))
if numberEntered != 0:
    if numberEntered % 2 == 0:
        numberSquare = numberEntered ** 2
        print(numberSquare, "Square")
    else:
        numberCube = numberEntered ** 3
        print(numberCube, "Cube.")
else:
    print("0^2 is not defined.")
print("-----------------------------------------------------")
# enter number and arithmetic operator and perform operation
print("Addition, enter +", "Subtraction enter -", "Multiplication  enter *", "Division enter /", sep="\n")
operatorList = {"+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul}
number1 = eval(input("ENTER NUMBER: "))
number2 = eval(input("ENTER NUMBER: "))
operator = input("Enter operator: ")

finalOutput = operatorList[operator](number1, number2)
print(finalOutput)
print("-----------------------------------------------------")
# to find if vowel or consonant
vowelList = ["a", "e", "i", "o", "u"]
chrEntered = input("Enter a english letter(a-z): ")
chrEnteredLower = chrEntered.lower()
if chrEnteredLower in vowelList:
    print("It is a vowel")
else:
    print("It is a consonant")

print("-----------------------------------------------------")
# find area or perimeter according to option inputted.
def circle(chrEntered):
    radius = eval(input("Enter radius: "))
    if chrEntered == "1":
        area = math.pi * (radius ** 2)
        print("area is", area)
    else:
        perimeter = math.pi * radius * 2
        print("perimeter is", perimeter)


def fourSidedPoly(chrEntered):
    if chrEntered == "2":
        length = eval(input("enter length: "))
        breadth = eval(input("enter breadth: "))
        areaOfRect = length * breadth
        print("area is", areaOfRect)
    else:
        sideLength = eval(input("Enter side length of square: "))
        areaOfSq = sideLength ** 2
        print("area is", areaOfSq)


print("INSTRUCTIONS", "Area of circle, enter 1", "Area of rectangle, enter 2", "Circumference of circle, enter 3",
      "Area of square, enter 4", sep="\n")
optionEntered = input("Enter option: ")
listEntered = {"1": circle, "2": fourSidedPoly, "3": circle, "4": fourSidedPoly}
listEntered[optionEntered](optionEntered)
print("-----------------------------------------------------")
# write a prgrm to find multiples of number out of given five numbers.
num1 = eval(input("Enter a number: "))
num2 = eval(input("Enter a number: "))
num3 = eval(input("Enter a number: "))
num4 = eval(input("Enter a number: "))
num5 = eval(input("Enter a number: "))
givenNum = eval(input("Enter number which will be used to check if the others are multiples or it: "))
if num1 % givenNum == 0:
    print(num1)
    if num2 % givenNum == 0:
        print(num2)
        if num3 % givenNum == 0:
            print(num3)
            if num4 % givenNum == 0:
                print(num4)
                if num5 % givenNum == 0:
                    print(num5)
            else:
                if num5 % givenNum == 0:
                    print(num5)
        elif num4 % givenNum == 0:
            print(num4)
            if num5 % givenNum == 0:
                print(num5)
        elif num5 % givenNum == 0:
            print(num5)
    elif num3 % givenNum == 0:
        print(num3)
        if num4 % givenNum == 0:
            print(num4)
            if num5 % givenNum == 0:
                print(num5)
    elif num4 % givenNum == 0:
        print(num4)
        if num5 % givenNum == 0:
            print(num5)
    elif num5 % givenNum == 0:
        print(num5)
elif num2 % givenNum == 0:
    print(num2)
    if num3 % givenNum == 0:
        print(num3)
        if num4 % givenNum == 0:
            print(num4)
            if num5 % givenNum == 0:
                print(num5)
        else:
            if num5 % givenNum == 0:
                print(num5)
    elif num4 % givenNum == 0:
        print(num4)
        if num5 % givenNum == 0:
            print(num5)
    elif num5 % givenNum == 0:
        print(num5)
elif num3 % givenNum == 0:
    print(num3)
    if num4 % givenNum == 0:
        print(num4)
        if num5 % givenNum == 0:
            print(num5)
    else:
        if num5 % givenNum == 0:
            print(num5)
elif num4 % givenNum == 0:
    print(num4)
    if num5 % givenNum == 0:
        print(num5)
elif num5 % givenNum == 0:
    print(num5)
else:
    print("none are multiples")
print("-----------------------------------------------------")

# Program to print nums backward in same line
for i in range(100, 50, -1):
    print(i, end=" ")
print("\n")
print("---------------------------------------------------")
# prgrm to print first five odd, even nums
print("odd""\t""even")
for n in range(1, 11):
    if n % 2 == 1:
        print(n, end="\t")
    else:
        print(n)
print("---------------------------------------------------")
