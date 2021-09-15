# prgrm 1 max min of five numbers
smallestTerm = biggestTerm = eval(input("Enter number 1 : "))
for m in range(2, 6):
    inputStatement = "Enter number " + str(m) + " : "
    term = eval(input(inputStatement))
    if term < smallestTerm:
        smallestTerm = term
    elif term > biggestTerm:
        biggestTerm = term
    else:
        pass
print(smallestTerm, biggestTerm, sep="\n")
print("--------------------------------------------------------------------")

# prgrm 2 sum of squares of 1-100
sumOfSquares = 0
for n in range(1, 101):
    termOne = n ** 2
    sumOfSquares += termOne
print(sumOfSquares)
print("--------------------------------------------------------------------")

# prgrm3 nums divisible by both 7,5 between 500-700
for o in range(500, 701):
    if o % 5 == 0 and o % 7 == 0:
        print(o, end="\t")
else:
    print()
print("--------------------------------------------------------------------")

# prgrm4 pattern
for p in range(0, 4):
    patternString = ""
    for q in range(4, p, -1):
        patternString += str(q) + "\t"
    print(patternString)
print("--------------------------------------------------------------------")

# prgrm 5 Fibonacci
fibonacciList = [0, 1]
noOfTerms = eval(input("Enter number of terms in sequence: "))
if noOfTerms > 2:
    limitOfRange = noOfTerms - 2
    for r in range(0, limitOfRange):
        nthTerm = fibonacciList[r] + fibonacciList[r + 1]
        fibonacciList.append(nthTerm)
    print(*fibonacciList)
else:
    if noOfTerms == 2:
        print(*fibonacciList)
    else:
        print(fibonacciList[0])
print("--------------------------------------------------------------------")

# prgrm 6 factorial of a number
numberEntered = eval(input("Enter number for which factorial to be found: "))
factorial = 1
if numberEntered == 1 or numberEntered == 0:
    print(1)
else:
    for s in range(2, numberEntered + 1):
        factorial *= s
    print(factorial)
print("--------------------------------------------------------------------")

# Q 7
# a) 20
#    22
#    24
#    26
#    28
# b) I
#    N
#    D
#    I
#    A
# c) 8
