# PROGRAM 3 SI
print("Program to calculate SI over a period of five years.")
timePeriod = 5
principle = eval(input("Enter amount: "))
ratePerAnnum = eval(input("Enter rate of interest/annum: "))

simpleInterest = principle * timePeriod * ratePerAnnum / 100

print("The simple interest over a period of five years is:", simpleInterest)
print("---------------------------------------------------------------------------------------")
