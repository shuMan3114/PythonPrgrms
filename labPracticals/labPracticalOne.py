# Q1
# to find area of triangle and rectangle
# finding area of triangle
import math

side = eval(input("Enter first side of triangle: "))
height = eval(input("Enter the height of the triangle: "))
area = 1 / 2 * side * height
print("Area of triangle is:", area)
# finding area of rectangle:
length = eval(input("Enter length of rectangle: "))
breadth = eval(input("Enter breadth of rectangle: "))
area = length * breadth
print("Area of rectangle is:", area)

# Q2
# a
twoA = (8 / 3) + 8 * 3
# b
twoB = math.sqrt(8 + 43)
# c
twoC = math.sqrt(8) + math.sqrt(43)
# d
twoD = 100 // 32

# Q3
dollars = eval(input("Enter value in dollars: "))
rupees = dollars * 80
print("Value in rupees is:", rupees)

# Q4
costOfGoods = eval(input("Enter the value of cost of goods: "))
revenueGenerated = eval(input("Enter the value of revenue generated: "))
operatingCosts = eval(input("Enter the value of operating cost: "))
netProfit = revenueGenerated - costOfGoods - operatingCosts
netProfitPercentage = netProfit / revenueGenerated * 100
grossProfit = revenueGenerated - costOfGoods
print("Net Profit:", netProfit, "\n" "Net profit %:", netProfitPercentage, "\n" "Gross Profit:", grossProfit)

# Q5
number = eval(input("Enter a number: "))  # Entering number
numberSquare = number ** 2
numberCube = int(math.pow(number, 3))
numberFour = int(math.pow(number, 4))
print(number, numberSquare, numberCube, numberFour, sep="\n")
