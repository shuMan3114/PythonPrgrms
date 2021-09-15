# Prgrm 1
lenOfList = eval(input("Enter num of numbers in list"))
numToIncrement = eval(input("Enter the number to add to list elements"))
ogList = []
incrementedList = []
for a in range(0, lenOfList):
    inputStatement = "Enter " + str(a + 1) + "number"
    termToPushL1 = eval(input(inputStatement))
    termToPushIncrement = termToPushL1 + numToIncrement
    ogList.append(termToPushL1)
    incrementedList.append(termToPushIncrement)
else:
    for b in range(0, lenOfList):
        print("OG Num", ogList[b], "incremented num", incrementedList[b])
    else:
        print("OG LIST", *ogList)
        print("INCREMENTED LIST", *incrementedList)

# prgrm 2
numList = []
reversedList = []
for c in range(0, lenOfList):
    inputStatement = "Enter " + str(c + 1) + "number"
    termToPush = eval(input(inputStatement))
    numList.append(termToPush)
    reversedList.insert(0, termToPush)
else:
    print("OG list", numList)
    print("Reversed list", reversedList)

# prgrm3
mergedList = []
lenOfListOne = eval(input("Enter length of first list"))
lenOfListTwo = eval(input("Enter length of second list"))
for d in range(1, lenOfListOne + lenOfListTwo + 1):
    if d <= lenOfListOne:
        inputStatement = "Enter " + str(d) + " number of List One"
        termToBePushed = eval(input(inputStatement))
        mergedList.append(termToBePushed)
    else:
        inputStatement = "Enter " + str(d - lenOfListOne) + " number of List Two"
        termToBePushed = eval(input(inputStatement))
        mergedList.append(termToBePushed)
else:
    print("List One is", mergedList[0:lenOfListOne])
    print("List Two is", mergedList[lenOfListOne: lenOfListTwo + lenOfListOne])
    print("merged list is", mergedList)

# prgrm4
inputtedList = eval(input("Enter a list of numbers from 1-12 make sure you in put i format : [num1, num2, ...]: "))
for e in range(0, len(inputtedList)):
    term = inputtedList[e]
    termIndex = inputtedList.index(term)
    if term > 10:
        inputtedList.remove(term)
        inputtedList.insert(termIndex, 10)
else:
    print(inputtedList)

# prgrm 5
lenOfList = eval(input("Enter number of strings in list: "))
ogStrList = []
finalStrList = []
for f in range(0, lenOfList):
    inputStatement = "Enter the " + str(f + 1) + " String: "
    ogString = input(inputStatement)
    ogStrList.append(ogString)
    stringSliced = ogString[1:]
    finalStrList.append(stringSliced)
else:
    print("Original list", ogStrList)
    print("List with first chars sliced ", finalStrList)

# prgrm 6
import random

lenOfList = eval(input("Enter length of list: "))
inputStatement = "Enter the number you suspect is in the list,[0," + str(lenOfList) + "]: "
numberSus = eval(input(inputStatement))
numList = []
trueList = []
for g in range(0, lenOfList):
    term = random.randint(0, lenOfList)
    numList.append(term)
    if term == numberSus and term not in trueList:
        trueList.append(term)
else:
    if len(trueList) == 0:
        print("Wrong Guess")
        print("List is", *numList)
    else:
        print("Correct Guess", "Number was repeated in list", numList.count(trueList[0]), "time/s.")
        print("List is", *numList)

# prgrm 7
# a)
integerList = []
for h in range(0, 50):
    integerList.append(h)
else:
    print("integer list 0-49", integerList)
# b)
squareList = []
for i in range(1, 51):
    squareOfI = i ** 2
    squareList.append(squareOfI)
else:
    print("Square list is ", squareList)
# c)
alphabetIndex = []
finalList = []
for j in range(97, 123):
    alphabetIndex.append(chr(j))
for k in range(0, 26):
    chrString = ""
    for l in range(0, k + 1):
        chrString += alphabetIndex[k]
    finalList.append(chrString)
else:
    print(len(finalList[-1]))
    print(finalList)

# prgrm8
lenOfList = eval(input("Enter length of both lists(have to be same): "))
listOne = []
listTwo = []
finalList = []
for m in range(0, lenOfList * 2):
    if m <= lenOfList:
        inputStatement = "Enter the " + str(m) + " number of list1: "
        term = eval(input(inputStatement))
        listOne.append(term)
    else:
        inputStatement = "Enter the " + str(m - lenOfList) + " number of list1: "
        term = eval(input(inputStatement))
        listTwo.append(term)
for n in range(0, lenOfList):
    finalList.append(listOne[n] + listTwo[n])
else:
    print("listOne:", listOne, "listTwo:", listTwo, "finalList:", finalList)

# prgrm 9
lenOfList = eval(input("Enter length of list: "))
originalList = []
swappedList = []
for o in range(0, lenOfList):
    inputStatement = "Enter " + str(o + 1) + " number: "
    term = eval(input(inputStatement))
    originalList.append(term)
for p in range(0, lenOfList - 1):
    swappedList.append(originalList[p])
else:
    swappedList.insert(0, originalList[lenOfList - 1])
    print("Original List: ", originalList, "\n""Swapped List", swappedList)

# prgrm 10
lenOfList = eval(input("Enter number of fractions: "))
num = []
denum = []
inputStatementNum = "Enter the num of the 1 fraction: "
inputStatementDenum = "Enter the denum of the 1 fraction: "
numerator = eval(input(inputStatementNum))
denominator = eval(input(inputStatementDenum))
num.append(numerator)
denum.append(denominator)
smallestFraction = numerator / denominator
smallestFractionIndex = 0
for q in range(1, lenOfList):
    inputStatementNum = "Enter the num of the " + str(q + 1) + " fraction: "
    inputStatementDenum = "Enter the denum of the " + str(q + 1) + " fraction: "
    numerator = eval(input(inputStatementNum))
    denominator = eval(input(inputStatementDenum))
    num.append(numerator)
    denum.append(denominator)
    fraction = numerator / denominator
    if fraction < smallestFraction:
        smallestFraction = fraction
        smallestFractionIndex -= smallestFractionIndex - q
else:
    print("Smallest fraction is ", num[smallestFractionIndex], "/", denum[smallestFractionIndex], sep="")

# prgrm 11
import random

lenOfList = eval(input("Enter length of list: "))
startingIndex = eval(input("Enter staring index: "))
endingIndex = eval(input("Enter the last index: "))
numList = []
for r in range(0, lenOfList):
    term = random.randint(0, lenOfList)
    numList.append(term)
print(numList)
print("max number", max(numList[startingIndex:endingIndex + 1]))
print("min number", min(numList[startingIndex:endingIndex + 1]))

# prgrm 12
import random

lenOfList = eval(input("Enter length of list: "))
numList = []
for s in range(0, lenOfList):
    term = random.randint(0, lenOfList)
    numList.append(term)
numList = numList*2
print(numList)

