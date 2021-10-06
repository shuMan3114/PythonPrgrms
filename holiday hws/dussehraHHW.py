# CONDITIONS AND LOOP PROGRAMS
# Q1
number = eval(input("Enter any number: "))
if(number > 0 or number < 0):
    if(number > 0):
        print("Positive number.")
    else:
        print("Negative number.")
else:
    print("Zero")

# Q2
n = eval(input("Enter the nth term: "))
prevTerm = 0
term = 1
for a in range(1,n):
    # good old switchero
    prevTerm, term = term, term + prevTerm
if(n==1):
    print(prevTerm)
else:
    print(term)

# Q3
n = eval(input("Enter the number of squares whose sum requird: "))
sumOfSqaures = (n*(n+1)*(2*n+1))/6
print(sumOfSqaures)

# Q4
n = eval(input("Enter the number of cubes: "))
for b in range(1,n+1):
    print(b**3)

# Q5
year = eval(input("Enter the year: "))
if( year%4 == 0):
    if(year%100 == 0):
        if(year%400 == 0):
            print("Not a leap year")
        else:
            print("Leap year")
    else:
        print("leap year")
else:
    print("Not a leap year")

# Q6
num = input("Enter a number: ").replace(".","")
n = 0
sumOfCubes = 0
while n < len(num):
    sumOfCubes += int(num[n])**3
    n += 1
if(int(num) == sumOfCubes):
    print("Armstrong number")
else:
    print("Not armstrong")

# Q7
n = eval(input("Enter the number of terms you want: "))
prevTerm = 0
term = 1
if(n>2):
    print(prevTerm, term, sep="\n")
    for b in range(1,n-1):
        prevTerm, term = term, term + prevTerm
        print(term)
if(n<=2):
    if(n==2):
        print(prevTerm, term, sep="\n")
    else:
        print(prevTerm)

# Q8
numToCheck = eval(input("Enter a prime number: "))
factors = 0
for c in range(2, int((numToCheck/2)+2)):
    if numToCheck%c == 0:
        print("Prime 404")
        break
else:
    if(factors == 0):
        print("Prime 200")

# Q9
for d in range(1,51):
    factors = 1
    for e in range(2, int((d/2)+2)):
        if(d%e == 0):
            factors +=1
    if(factors ==1 ):
        print(d)

# Q10
vowel = ['a','e','i','o','u']
charector = input("Enter a alphabet in any case").lower()
if charector in vowel:
    print("vowel")
else:
    print("consonent")

# LIST PROGRAMS
# Q1
listGiven = list(eval(input("Enter the list values separated by commas: ")))
lastElement = listGiven.pop()
firstElement = listGiven.pop(0)
listGiven.insert(0, lastElement)
listGiven.append(firstElement)
print(listGiven)

# Q2
listGiven = list(eval(input("Enter the list values separated by commas: ")))
lastElement = listGiven.pop()
firstElement = listGiven.pop(0)
listGiven.insert(0,lastElement)
listGiven.append(firstElement)
print(listGiven)

# Q3
listGiven = list(eval(input("Enter the list values separated by commas: ")))
swapList = list(eval(input("Enter the elements you want to swap seperated by commas: ")))
indexList = [listGiven.index(swapList[1]),listGiven.index(swapList[0])]
listGiven[indexList[0]], listGiven[indexList[1]]= swapList[0],swapList[1]
print(listGiven)

# Q4
listGiven = list(eval(input("Enter the list values separated by commas: ")))
lenOfList = 0
for f in listGiven:
    lenOfList+=1
else:
    print(lenOfList)

# Q5
listGiven = list(eval(input("Enter the list values separated by commas: ")))
print(listGiven.reverse())
listReversed = reversed(listGiven)
listReversedSlice = listGiven[::-1]
print(listReversed,listReversedSlice)

# Q6
listGiven = list(eval(input("Enter the list values separated by commas: ")))
print(sum(listGiven))

# Q7
listGiven = list(eval(input("Enter the list values separated by commas: ")))
product =1
for g in listGiven:
    product *= g
print(product)

# Q8
listGiven = list(eval(input("Enter the list values separated by commas: ")))
listGiven.sort()
print(listGiven[0])

# Q9
listGiven = list(eval(input("Enter the list values separated by commas: ")))
print(min(listGiven))

# Q10
listGiven = list(eval(input("Enter the list values separated by commas: ")))
largestElement = 0
for h in listGiven:
    if(h>largestElement):
        largestElement=h
else:
    print(largestElement)

# STRING PROGRAMS
# Q1
sentence = input("Enter a sentence: ").split(" ")
print(sentence[-1])

# Q2
sentence = input("Enter a string: ")
lenOfSentence = 0
for i in sentence:
    lenOfSentence+=1
else:
    print(lenOfSentence)

# Q3
sentence = list(input("Enter a string: "))
reversedSentence = []
for j in sentence:
    reversedSentence.insert(0, j)
print("".join(reversedSentence))

# Q4
sentence = list(input("Enter a string: "))
reversedSentence = []
k=0
while k< len(sentence):
    reversedSentence.insert(0, sentence[k])
    k+=1
print("".join(reversedSentence))

# Q5
sentence = list(input("Enter a string: "))
reversedSentence = sentence[::-1]
print("".join(reversedSentence))

# Q6
sentence = list(input("Enter a string: ").lower())
reversedSentence = "".join(sentence[::-1])
if("".join(sentence)== reversedSentence):
    print("pallindrome")
else:
    print("not pallindrome")

# Q7
sentence = list(input("enter a string: "))
sentence[0], sentence[-1]= sentence[-1], sentence[0]
print("".join(sentence))

# Q8
sentence = input("enter a string: ").split()
for l in range(0, len(sentence)):
    word =sentence[l]
    firstLetter = word[0].upper()
    lastLetter = word[-1].upper()
    word = firstLetter + word[1:-1]+lastLetter
    sentence[l]=word
print(" ".join(sentence))

# Q9
sentence = input("enter a string: ").lower()
wordList = sentence.split()
specCharList = list(sentence)
wordQuery = input("Enter a word to find in the sentence: ").lower()
if(wordQuery in wordList or wordQuery in specCharList):
    print("200")
else:
    print("404")

# Q10
sentence = input("enter a string: ").lower()
vowel = ['a','e','i','o','u']
print(len(list(filter(lambda x: x in vowel, sentence))))
