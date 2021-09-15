# import math
#
# # prgrm1
# numberGiven = eval(input("Enter a number: "))
# divisorList = []
# for a in range(1, numberGiven + 1):
#     if numberGiven % a == 0:
#         divisorList.append(a)
# else:
#     print("The divisors of", numberGiven, "are: ", *divisorList, sep=" ")
#
# # prgrm2
# print("Enter SI for Simple Interest", "Enter CI for Compound Interest", sep="\n")
# modeSelected = input("Enter method: ").upper()
# principle = eval(input("Enter Principle: "))
# timePeriod = eval(input("Enter TimePeriod(Yrs): "))
# rateAnnum = eval(input("Enter rate%/annum: "))
# if modeSelected == "SI":
#     SI = principle * timePeriod * rateAnnum / 100
#     print("Simple Interest is", SI)
# else:
#     intermediateCI = (1 + rateAnnum / 100) ** timePeriod
#     CI = principle * intermediateCI
#     print("Compound Interest is", CI)
#
# # prgrm3
# print("Area of Circle, Enter C", "Area of Square, Enter S", "Area of Rectangle, Enter R", sep="\n")
# modeSelected = input("Enter mode: ").upper()
# if modeSelected == "C":
#     radius = eval(input("Enter radius: "))
#     area = math.pi * radius
#     print(area)
# elif modeSelected == "S":
#     side = eval(input("Enter side length: "))
#     area = side ** 2
#     print(area)
# else:
#     length = eval(input("Enter side length: "))
#     breadth = eval(input("Enter breadth length: "))
#     area = length * breadth
#     print(area)
#
# # prgrm4
# number = input("Enter a number: ")
# reversedNum = ""
# for b in range(-1, -len(number) - 1, -1):
#     term = number[b]
#     reversedNum += term
# else:
#     print(reversedNum)
#     sumOfReversed = eval(number) + eval(reversedNum)
#     print("Sum of reversed num and num is", sumOfReversed)
#
# # prgrm5
# numOfNumber = eval(input("Enter how many numbers to be entered: "))
# numberList = []
# for c in range(0, numOfNumber):
#     inputStatement = "Enter " + str(c + 1) + " number: "
#     termToBePushed = eval(input(inputStatement))
#     numberList.append(termToBePushed)
# sortedList = []
# for d in range(0, numOfNumber):
#     if d != numOfNumber - 1:
#         termToBeTested = numberList[0]
#         for e in range(0, len(numberList)):
#             if termToBeTested > numberList[e]:
#                 termToBeTested = numberList[e]
#         numberList.remove(termToBeTested)
#         sortedList.append(termToBeTested)
#     else:
#         sortedList.append(numberList[0])
# else:
#     print("lowest", sortedList[0])
#     print("second lowest", sortedList[1])
#
# # prgrm6
# # To dumb
# studentName = input("Enter student name: ")
# studentClass = input("enter student class: ")
# studentRolNo = input("enter student roll no: ")
# print("Student Name :", studentName, "\n""Student Class :", studentClass,"\n""Student Roll No :", studentRolNo)
#
# # prgrm 7
# numberEntered = eval(input("Enter a number: "))
# sumOfDivisors = 0
# for f in range(1, numberEntered + 1):
#     if numberEntered % f == 0:
#         sumOfDivisors += f
# else:
#     if sumOfDivisors == (numberEntered + 1):
#         print("Number is prime.")
#
# # prgrm8
# vowels = ["a", "e", "i", "o", "u"]
# consonants = []
# for g in range(97, 123):
#     if chr(g) not in vowels:
#         consonants.append(chr(g))
# numbers = ["1", "2", "3", "3", "4", "5", "6", "7", "8", "9", "0"]
# numOfVowels = 0
# numOfConsonants = 0
# numOfNumbers = 0
# numOfSpecChar = 0
# stringEntered = input("Enter a string: ").lower()
# for h in range(0, len(stringEntered)):
#     if stringEntered[h] in vowels:
#         numOfVowels += 1
#     elif stringEntered[h] in consonants:
#         numOfConsonants += 1
#     elif stringEntered[h] in numbers:
#         numOfNumbers += 1
#     else:
#         numOfSpecChar += 1
# else:
#     print("num of vowels", numOfVowels, "\n""num of consonants", numOfConsonants, "\n""number of numbers", numOfNumbers,
#           "\n""miscellaneous", numOfSpecChar)
#
# # prgrm9
# alphabet = []
# for i in range(97, 123):
#     alphabet.append(chr(i))
# sentenceEntered = input("Enter a sentence: ").lower()
# wordsSplit = sentenceEntered.split()
# wordInSentence = []
# for j in range(0, len(wordsSplit)):
#     word = wordsSplit[j]
#     wordSyllableList = []
#     for k in range(0, len(word)):
#         if word[k] in alphabet:
#             wordSyllableList.append(word[k])
#     newWord = ""
#     for l in range(0, len(wordSyllableList)):
#         newWord += wordSyllableList[l]
#     if newWord != "":
#         wordInSentence.append(newWord)
# duplicateWords = []
# for m in range(0, len(wordInSentence)):
#     if wordInSentence[m] not in duplicateWords:
#         duplicateWords.append(wordInSentence[m])
# for n in range(0, len(duplicateWords)):
#     duplicateCount = wordInSentence.count(duplicateWords[n])
#     print(duplicateWords[n], duplicateCount, sep=": ", end="    -+-     ")
# print()
#
# # prgrm 10
# fibonacci = [0, 1]
# numberOfTerms = eval(input("Enter number of terms: "))
# if numberOfTerms > 2:
#     for p in range(1, numberOfTerms - 1):
#         nthTerm = fibonacci[p - 1] + fibonacci[p]
#         fibonacci.append(nthTerm)
#     else:
#         print(*fibonacci)
# else:
#     if numberOfTerms == 1:
#         print(fibonacci[0])
#     else:
#         print(*fibonacci)
#
# # prgrm 11
# stringEntered = input("Enter a word: ").lower()
# stringReversed = ""
# for q in range(-1, -len(stringEntered) - 1, -1):
#     stringReversed += stringEntered[q]
# else:
#     if stringEntered == stringReversed:
#         print("Palindrome")
#     else:
#         print("Not a palindrome")
#
# # prgrm 12
# stringEntered = input("Enter String: ")
# print(stringEntered.lower(), stringEntered.upper(), stringEntered.swapcase())
#
# # prgrm 13
# stringEntered = input("Enter a sentence: ").replace(" ", "-")
# print(stringEntered)
#
# # prgrm14 same as prgrm 17..
#
# # prgrm 15
# numOfNumber = eval(input("Enter how many numbers to be entered: "))
# numberList = []
# for r in range(0, numOfNumber):
#     inputStatement = "Enter " + str(r + 1) + " number: "
#     termToBePushed = eval(input(inputStatement))
#     numberList.append(termToBePushed)
# sortedList = []
# for s in range(0, numOfNumber):
#     if s != numOfNumber - 1:
#         termToBeTested = numberList[0]
#         for t in range(0, len(numberList)):
#             if termToBeTested > numberList[t]:
#                 termToBeTested = numberList[t]
#         numberList.remove(termToBeTested)
#         sortedList.append(termToBeTested)
#     else:
#         sortedList.append(numberList[0])
# else:
#     print("lowest", sortedList[0])
#     print("Largest", sortedList[-1])
#
# # prgrm 16
# numOfNumber = eval(input("Enter how many numbers to be entered: "))
# numberList = []
# for u in range(0, numOfNumber):
#     inputStatement = "Enter " + str(u + 1) + " number: "
#     termToBePushed = eval(input(inputStatement))
#     numberList.append(termToBePushed)
# sortedList = []
# for v in range(0, numOfNumber):
#     if v != numOfNumber - 1:
#         termToBeTested = numberList[0]
#         for u in range(0, len(numberList)):
#             if termToBeTested > numberList[u]:
#                 termToBeTested = numberList[u]
#         numberList.remove(termToBeTested)
#         sortedList.append(termToBeTested)
#     else:
#         sortedList.append(numberList[0])
# else:
#     print("third smallest", sortedList[2])
#     print("third largest", sortedList[-3])
#
# # prgrm 17
# duplicateArrayItems = []
# array = []
# numOfNums = eval(input("Enter the number of values in list(make sure list will have duplicates): "))
# for w in range(0, numOfNums):
#     inputStatement = "Enter " + str(w + 1) + " item: "
#     arrayItem = input(inputStatement)
#     if arrayItem not in array:
#         array.append(arrayItem)
#     else:
#         duplicateArrayItems.append(arrayItem)
#         array.append(arrayItem)
# for y in range(0, len(duplicateArrayItems)):
#     numOfTimes = array.count(duplicateArrayItems[y])
#     for z in range(0, numOfTimes):
#         array.remove(duplicateArrayItems[y])
#         array.append(duplicateArrayItems[y])
# else:
#     print(array)
#
# # prgrm 19
# subList = ["english", "mathematics", "science"]
# paramList = ["rollNo", "name"]
# subMarks = []
# studentInfoAndMarks = []
# totalMarks = 0
# for a in range(0, 5):
#     if a < 2:
#         inputStatement = "Enter student " + paramList[a] + " : "
#         param = input(inputStatement)
#         studentInfoAndMarks.append(param)
#     else:
#         inputStatement = "Enter student marks in " + subList[a - 2] + " : "
#         individualSubMarks = eval(input(inputStatement))
#         totalMarks += individualSubMarks
#         subMarks.append(individualSubMarks)
# else:
#     studentInfoAndMarks.append(subMarks)
#     avgMarks = totalMarks/3
#     studentInfoAndMarks.append(avgMarks)
#     print(studentInfoAndMarks)
