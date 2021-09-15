# Q1
# linear search -->> traverse list once..
numCheck = eval(input("Enter the number you want to check: "))
L1 = [ 10,15,21,2 ,18 ,4 ,31,13 ,5 ,23 , 64, 29 ]
print("List items are: ", *L1)
numIndex = -1
for a in range(0, len(L1)):
    if(numCheck == L1[a]):
        numIndex = a
else:
    if(numIndex >= 0):
        print("The Number you entered was:",numCheck, "\n""Found at index",numIndex)
    else:
        print("The Number you entered was:",numCheck, "\n""Found at index: None")

# Q2
# CHECKING DUPLICATES
L = [3,21,5,6,3,8,21,6]
numCheck = eval(input("Enter the number to check: "))
if(L.count(numCheck)>0):
    print("Number is repeated ",L.count(numCheck),"times.")
else:
    print("Number wasnt repeated")

# Q3
L2=[ "RINKU", "ASHWINI","VIJAY","AMAR","AARYA"]
# TRAVERSING TO FIND A
for b in range(0, len(L2)):
    string = L2[b].upper()
    if(string[0] == "A"):
        print(string)
