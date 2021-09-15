# 6.12
mergedList = []
lenOfListOne = eval(input("Enter length of first list"))
lenOfListTwo = eval(input("Enter length of second list"))
for a in range(1, lenOfListOne + lenOfListTwo + 1):
    if a <= lenOfListOne:
        inputStatement = "Enter " + str(a) + " number of List One"
        termToBePushed = eval(input(inputStatement))
        mergedList.append(termToBePushed)
    else:
        inputStatement = "Enter " + str(a - lenOfListOne) + " number of List Two"
        termToBePushed = eval(input(inputStatement))
        mergedList.append(termToBePushed)
else:
    print("List One is", mergedList[0:lenOfListOne])
    print("List Two is", mergedList[lenOfListOne: lenOfListTwo + lenOfListOne])
maxNum = max(mergedList)
indexOfMax = mergedList.index(maxNum)
if indexOfMax >= lenOfListOne:
    indexOfMax = indexOfMax - lenOfListOne
    print("Max Number is in List2 and it is", maxNum, "its index in list2 is", indexOfMax)
else:
    print("Max Number is in List1 and it is", maxNum, "its index in list1 is", indexOfMax)

# 6.11
