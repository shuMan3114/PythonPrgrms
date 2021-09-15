# # prgrm 7.1
# marksDictionaryOne = {}
# for e in range(0, 4):
#     rollNo = int(input("Enter Student Roll No: "))
#     marks = eval(input("Enter marks of Student: "))
#     marksDictionaryOne[rollNo] = marks
# print(marksDictionaryOne)
#
# # prgrm 7.2
# if 2 not in marksDictionaryOne:
#     print("Roll No: 2 does not exist")
# else:
#     if marksDictionaryOne[2] > 75:
#         print("Marks above 75")
#     else:
#         print("marks below 75")
#
# # prgrm 7.3
# import random
#
# nameList = ["Lughaidh", "Ander", "Lea", "Delia", "Abidan", "Umberto", "Briana", "Diane", "Ghyslaine", "Italo"]
# phoneDictionary = {}
# for a in range(0, 10):
#     term = ""
#     b = 0
#     while b < 10:
#         term += str(random.randint(0, 9))
#         b += 1
#     phoneDictionary[nameList[a]] = int(term)
# for c in phoneDictionary:
#     print(c, ":", phoneDictionary[c])
#
# # prgrm 7.4
# marksDictionaryTwo = {}
# for d in range(1, 11):
#     term = random.randint(0, 11)
#     if term == 4:
#         marksDictionaryTwo[d] = 89.9
#     else:
#         marksDictionaryTwo[d] = term + 80
# if 89.9 in marksDictionaryTwo.values():
#     print("someone has scored 89.9")
# else:
#     print("No one scored 89.9")
#
# # prgrm 7.5
# marksDictionaryThree = {}
# lenOfDict = eval(input("Number of Students: "))
# for e in range(0, lenOfDict):
#     rollNo = int(input("Enter Student Roll No: "))
#     marks = eval(input("Enter marks of Student: "))
#     marksDictionaryThree[rollNo] = marks
# print(marksDictionaryThree)
#
# # prgrm 7.6
# studentMarksToModify = int(input("Enter roll no of student whose marks to be modified: "))
# if studentMarksToModify not in marksDictionaryThree:
#     print("Creating new student entry in dictionary")
#     marksDictionaryThree[studentMarksToModify] = eval(input("Enter marks: "))
#     print(marksDictionaryThree)
# else:
#     marksDictionaryThree[studentMarksToModify] = eval(input("Enter modified marks: "))
#     print("Modified marks in student")
#     print(marksDictionaryThree)
#
# # prgrm 7.7
# keys = ["one", "two", "three"]
# values = [1, 2, 3]
# numerals = {}
# for f in range(0, 3):
#     numerals[keys[f]] = values[f]
# print(numerals)
#
# # prgrm 7.8
# print("Creating new student entry in dictionary")
# studentMarksToModify = int(input("Enter roll no of student: "))
# marksDictionaryThree[studentMarksToModify] = eval(input("Enter marks: "))
# print(marksDictionaryThree)
# Q4
totalNumSections = eval(input("Enter the number of sections in XI: "))
finalList = []
for z in range(0, totalNumSections):
    term = []
    section = input("Enter the section: ").upper()
    term.append(section)
    finalList.append(term)
# OK SOO YOU INPUT THE NUMBER OF FIELDS AND THEN KEEP THEM AS A LIST...
# AFTER KEEPING THEM AS A LIST YOU ASK USER WHICH FIELD BELONGS TO WHICH..
# AND YOU APPEND THE DIFFERENT VALUES IN A SEPERATE LIST AND DO IT..
totalNumOfStreams = eval(input("Enter total number of streams: "))
for a in range(0, totalNumOfStreams):
    stream = input("Enter the stream: ").upper()
    section = input("Enter the corresponding section: ").upper()
    for b in range(0, totalNumSections):
        sectionList = finalList[b]
        if (sectionList[0] == section):
            sectionList.append(stream)
# else:
#     print(finalList)
sectionsDictionary = {}
for c in range(0, totalNumSections):
    sectionStreams = finalList[c]
    if (len(sectionStreams) == 2):
        sectionsDictionary[sectionStreams[0]] = sectionStreams[1]
    elif (len(sectionStreams) > 2):
        sectionsDictionary[sectionStreams[0]] = sectionStreams[1::]
    else:
        print("Warning section has no stream..")
print("CLASS", "\t", "SECTION", "\t", "STREAM")
for section in sectionsDictionary:
    sectionValue = sectionsDictionary[section]
    if isinstance(sectionValue, list):
        for d in range(0, len(sectionValue)):
            print("XI", "\t", section, "\t", sectionValue[d])
    else:
        print("XI", "\t", section, "\t", sectionValue)
