# prgrm 1
import random

sampleList = []
for c in range(0, 10):
    term = random.randint(0, 30)
    sampleList.append(term)


def modifyList(givenList):
    elementToModify = eval(input("Enter the element which you want to modify: "))
    newElement = eval(input("Enter the modified element: "))
    indexToInsert = givenList.Index(elementToModify)
    givenList.pop(indexToInsert)
    givenList.insert(indexToInsert, newElement)
    return givenList


def appendElement(givenList, keyValue):
    if keyValue == 1:
        elementToPush = eval(input("Enter element to append: "))
        givenList.append(elementToPush)
        return givenList
    else:
        lenOfList = eval(input("Enter number of elements to be appended: "))
        for a in range(0, lenOfList):
            inputStatement = "Enter the " + str(a + 1) + " element: "
            variable = eval(input(inputStatement))
            givenList.append(variable)
        return givenList


def insertElement(givenList):
    elementIndex = eval(input("Enter element index: "))
    elementToInsert = eval(input("Enter element to insert: "))
    givenList.insert(elementIndex, elementToInsert)
    return givenList


def deleteElementValue(givenList):
    element = eval(input("Enter the element to delete: "))
    if givenList.count(element) > 1:
        print("There are", givenList.count(element), "similar elements in the list.")
        timesToBeRemoved = eval(input("Enter number of times to delete the element: "))
        for b in range(0, timesToBeRemoved):
            givenList.remove(element)
        return givenList
    else:
        givenList.remove(element)
        return givenList


def deleteElementPosition(givenList):
    indexToDelete = eval(input("Enter index of element to delete: "))
    givenList.pop(indexToDelete)
    return givenList


def listMethod(givenList):
    listAction = {1: appendElement, 2: insertElement, 3: appendElement, 4: modifyList, 5: deleteElementPosition,
                  6: deleteElementValue, 7: sorted, 8: sorted}
    keyValue = eval(input("Enter mode: "))
    if keyValue == 1 or keyValue == 3:
        newList = listAction[keyValue](givenList, keyValue)
        return newList
    elif keyValue == 8:
        newList = listAction[keyValue](givenList, reverse=True)
        return newList
    elif keyValue == 0:
        givenList.append("0")
        return givenList
    elif keyValue == 9:
        return givenList
    elif keyValue == 2 or (4 <= keyValue <= 9):
        newList = listAction[keyValue](givenList)
        return newList
    else:
        print("Please enter valid mode")
        return givenList


print("Enter 0 to exit..")
print("Enter 1 to append single element in list")
print("Enter 2 to insert element in list")
print("Enter 3 to append list of elements in list")
print("Enter 4 to insert element at a particular index(and delete existing element) in list")
print("Enter 5 to delete an element using its position in list")
print("Enter 6 to delete an element using its value in list")
print("Enter 7 to sort elements in ascending order")
print("Enter 8 to sort elements in descending order")
print("Enter 9 to display list")
breakVariable = 1
while breakVariable == 1:
    print(sampleList)
    sampleList = listMethod(sampleList)
    if sampleList[-1] == "0":
        sampleList.pop()
        print(sampleList)
        breakVariable = 0

# prgrm 2
print("Enter 1 to save student avg marks into list else enter 0: ")
flowVariable = eval(input("Enter mode: "))
if flowVariable == 1 or flowVariable == 0:
    marksList = []
    n = eval(input("Enter number of students"))
    sumOfMarks = 0
    for c in range(0, n):
        inputStatement = "Enter the marks of " + str(c + 1) + " student: "
        marks = eval(input(inputStatement))
        sumOfMarks += marks
        marksList.append(marks)
    avgMark = sumOfMarks / n
    if flowVariable == 1:
        marksList.append("Avg Marks: " + str(avgMark))
        print(marksList)
    else:
        print(marksList)
        print("Avg Marks:", avgMark)
else:
    print("Enter valid mode")
