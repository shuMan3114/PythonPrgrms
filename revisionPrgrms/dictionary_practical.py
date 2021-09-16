# Q8
dictionary = {"one": 1, "two": 2,"three": 3}
Vals = dictionary.values()
Vals.sort()
print(Vals[-1], Vals[-2])


# Q9
# w3resource so um if we can input the corresponding chr with index using for loop we can do it
stringToCheck = input("Enter the string")
chrIndexDictionary = {}
for a in range(0, len(stringToCheck)):
    if(stringToCheck[a] not in chrIndexDictionary.keys()):
        chrIndexDictionary[stringToCheck[a]] = a

print(chrIndexDictionary)

# Q10
import random

nameList = ["Lughaidh", "Ander", "Lea", "Delia", "Abidan", "Umberto", "Briana", "Diane", "Ghyslaine", "Italo"]
phoneDictionary = {}
for a in range(0, 10):
    term = ""
    b = 0
    while b < 10:
        term += str(random.randint(0, 9))
        b += 1
    phoneDictionary[nameList[a]] = int(term)

# Add new
phoneDictionary["Ram"] = "2345678901"

# Del
del phoneDictionary["Ram"]


phoneDictionary["Umberto"] = "1234567890"

if("Ram" in phoneDictionary.keys()):
    print("Exists")

# phoneDictionary = sorted(phoneDictionary)
# sorted does not work --- for dictionary manual sorting in keys is optimal


for c in phoneDictionary:
    print(c, ":", phoneDictionary[c])

# CASE STUDY --
n = eval(input("Enter the number of students"))
studentDetails = {}
for d in range(0, n):
    studentRollNo = eval(input("Enter student roll no: "))
    studentName = input("Enter the student name: ")
    studentPercentage = {"Total": 0, "Physics": 0, "Chemistry": 0, "Mathematics": 0, "IP": 0}
    for e in studentPercentage:
        inputStatement = "Enter the "+ e+ " percentage: "
        percentage = eval(input(inputStatement))
        studentPercentage[e] = percentage
    nestedDictionary = {"rollNo" : studentRollNo, "name": studentName, "percentage": studentPercentage}
    if(studentRollNo not in studentDetails.keys()):
        studentDetails[studentRollNo] = nestedDictionary
    else:
        print("rollNo already exists.")

# Query using rollNo:
rollQuery = eval(input("Enter the needed roll no: "))
if(rollQuery in studentDetails.keys()):
    outputDict = studentDetails[rollQuery]
    print("Roll No:",outputDict["rollNo"] ,"\n""Name:",outputDict["name"],"\n""Percentage",outputDict["percentage"])

# display results
for f in studentDetails:
    studentDictionary = studentDetails[f]
    print("Roll No:", studentDictionary["rollNo"] , "Name: ", studentDictionary["name"] ,"Result:", studentDictionary["percentage"])


# find da topper
topMarks = {"Total": 0, "Physics": 0, "Chemistry": 0, "Mathematics": 0, "IP": 0}
topRolls = {"Total": [0], "Physics": [0], "Chemistry": [0], "Mathematics": [0], "IP": [0]}
for g in studentDetails:
    outputDict = studentDetails[g]
    percentageDict = outputDict["percentage"]
    for h in percentageDict:
        rolls = topRolls[h]
        if(topMarks[h] < percentageDict[h]):
            topMarks[h] = percentageDict[h]
            for i in range(0, len(rolls)):
                rolls.pop()
            rolls.append(outputDict["rollNo"])
        elif(topMarks[h] == percentageDict[h]):
            rolls.append(outputDict["rollNo"])

for j in topRolls:
    rolls = topRolls[j]
    if(len(rolls) >1):
        topperNames = []
        for k in range(0, len(rolls)):
            topperNames.push(rolls[k])
        print(i, "Joint toppers:", *topperNames, "with marks:",topMarks[j])
    else:
        topperFellow = studentDetails[rolls[0]]
        topperName = topperFellow["name"]
        print(j,"Topper:",topperName,"with marks:",topMarks[j])