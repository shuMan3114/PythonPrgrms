# Q 9
# a)
lenOflist = eval(input("Enter the number of items you want to enter in the list: "))
finalList = []
for a in range(0, lenOflist):
    inputStatement = "Enter the "+ str(a+1) + " number: "
    term = eval(input(inputStatement))
    if(term % 2 == 0):
        finalList.append(term)
else:
    print(finalList)

# b)
secondLgstElmt = sorted(finalList)[-2]
prin(secondLgstElmt)

# c)
L1 = [11,-1,22,-3,33,55,44,-50,46,101,77,-100,42]
for b in range(0, len(L1)):
    if(L1[b] < 0 or L1[b] % 2 == 1):
        L1.pop(b)
else:
    print(L1)

# d)
L2 = [10,20,30,40,10,50,10]
numberToCount = eval(input("Enter the number: "))
if(L2.count(numberToCount) != 0):
    print(L2.count(numberToCount))
else:
    print("No occurences")

# Q8
L3=[]
# a) list.append(num)
L3.append(20)
# b) list.insert(index, value)
L3.insert(0, 40)
# c) list.extend(elements separeted by comma)
L3.extend(12,20,30,40)
# d) list.index(element)
L3.index(12)
# e) list.remove(element)
L3.remove(12)
# f) list.sort() --> ascending order , list.sort(reverse = True) --> descending order
L3.sort() 
L3.sort(reverse=True)
# g) sorted(list , reverse= False) --> ascending order , sorted(list, reverse=True) --> descending order
sorted(L3) 
sorted(L3, reverse=True)
# h) list.reverse()
L3.reverse()

# Q7
L4 = ["Hello", "World"]
L5 = L4

# Q6
L1 = list("COMPUTER")
extractionOne = L1[1:4]
extractionTwo = L1[3::]
extractionThree = []
for c in range(0,len(L1)):
    if(c%2 == 1):
        extractionThree.append(L1[c])
else:
    maxLen = eval(input("Enter how many odd position you want: "))
    print(extractionThree[0:maxLen])
extractionFour = L1[0:4]
extractionFive = L1[-1]
extractionSix = L1[0: len(L1)-2]
extractionSeven = L1[-3: -1]

# Q5
# Operations on lists == Replication , Concatination , Membership testing, Slicing, Indexing

# Q4
stringToTraverse = "COMPUTER"
index = eval(input("Enter the desired index: "))
length = len(stringToTraverse)
if(index>= -length and index < length):
    print(stringToTraverse[index])
else:
    if(index >= length):
        rem = index % length
        quotient = int(index / length)
        if(quotient % 2 == 0):
            print(stringToTraverse[rem])
        else:
            print(stringToTraverse[-rem])
    elif(index < -length):
        positiveRem = (-index) % length
        quotient = int((-index)/length)
        if(quotient % 2 == 0):
            print(stringToTraverse[-positiveRem])
        else:
            print(stringToTraverse[positiveRem])

# Q3
emptyList = list()
sequenceList = list("STRING")
userInputtedList = list(eval(input("Enter the values of list seperated by commas")))

# Q2
diffDatatypes = [1, "2", [3,4]]
charList = ["a", "b", "c"]
stringList = ["1", "2", "3", "4"]
longList = []
for d in range(0, 101):
    longList.append(d**2)

# Q1
# A list is a collection of data-types enclosed between square-brackets and seperated by commas. Lists can be operated on and can be traversed,etc
emptyList = list()
integerList = [1,2,3,4,5]
