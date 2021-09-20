print("Name : Himanshu Udupi")
print("Class XI B")
print("ROLL 11")
# q1
lenOfList = eval(input("Enter length of the list: "))
ogList = []
modifiedList = []
for a in range(0, lenOfList):
    inputStatement = "Enter the "+ str(a+1)+" number: "
    number = eval(input(inputStatement))
    if(number %2 ==0):
        newNum = number + 10
    else:
        newNum = number + 5
    ogList.append(number)
    modifiedList.append(newNum)
else:
    print(ogList)
    print(modifiedList)

# q2
lenOfList = eval(input("Enter the length of list: "))
listInput = []
duplicateInput = []
uniqueInput= []
for b in range(0, lenOfList):
    inputStatement = "Enter the "+ str(b+1)+" number: "
    number = eval(input(inputStatement))
    listInput.append(number)
for c in range(0, lenOfList):
    numberToCheck = listInput[c]
    if(listInput.count(numberToCheck) > 1):
        if(numberToCheck not in duplicateInput):
            duplicateInput.append(numberToCheck)
    else:
        uniqueInput.append(numberToCheck)
print("duplicates",duplicateInput)
print("unique",uniqueInput)


# q3
# {admissionNum : {admissionNum : admNum, rollNo: roll, name: name, percentage: percentage}}
n = eval(input("Enter the number of students: "))
studentDetails = {}
for d in range(0, n):
    admNum = input("Enter Admission num: ")
    rollNo = eval(input("Enter student roll no: "))
    name = input("Enter the student name: ")
    percentage = eval(input("Enter the total percentage: "))
    if(admNum not in studentDetails.keys()):
        studentDetails[admNum] = {admNum : admNum, rollNo: rollNo, name: name, percentage: percentage}
    else:
        print("Student already exists")

studentQuery = input("enter admission number")
if( studentQuery in studentDetails.keys()):
    print(studentDetails[studentQuery])
else:
    print("Not exist")


# q4
numToWords = { 1: "One", 2:"Two", 3:"Three", 4: "Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}

numInput = input("Enter the number: ")

wordForm = ""
for f in range(0 , len(numInput)):
    dictionaryKey = int(numInput[f])
    wordForm += numToWords[dictionaryKey]+" "
else:
    print(wordForm)