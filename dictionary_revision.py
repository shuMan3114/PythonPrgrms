# Q5 
# dictionary.keys() -->> gets the keys in the given diction
# dictionary.items() -->> gets all the items from the dictionary
# dictionary.values() -->> gets only the values of the given dictionary,
# dictionary.update({key : value}) -->> updates a certain key in the dictionary
# del dictionary[key] -->> deletes a certain key or can delete the dictionary if statement is del dictionary
# dictionary.pop(index)-->> pops the last item or can pop item according to index given
# dictionary.popitem() -->> pops particular item
# len(dictionary) -->> returns length of dicitonary
# dictionary.clear() -->> returns a empty dictionary : {}
# dictionary.get() -->> gets the values , keys in dictionary


# Q4
totalNumSections = eval(input("Enter the number of sections in XI: "))
finalList = []
# CREATING NESTED LISTS HAVING FIRST VALUE AS SECTION
for z in range(0, totalNumSections):
    term = []
    section = input("Enter the section: ").upper()
    term.append(section)
    finalList.append(term)
totalNumOfStreams = eval(input("Enter total number of streams: "))
# INPUT STREAM TO THE CORRESPONDING SECTION
for a in range(0, totalNumOfStreams):
    stream = input("Enter the stream: ").upper()
    section = input("Enter the corresponding section: ").upper()
    for b in range(0, totalNumSections):
        sectionList = finalList[b]
        if(sectionList[0] == section):
            sectionList.append(stream)
sectionsDictionary = {}
# CREATE DICTIONARY
for c in range(0, totalNumSections):
    sectionStreams = finalList[c]
    if(len(sectionStreams) == 2):
        sectionsDictionary[sectionStreams[0]] = sectionStreams[1]
    elif(len(sectionStreams) > 2):
        sectionsDictionary[sectionStreams[0]] = sectionStreams[1::]
    else:
        print("Warning section has no stream..")
# DISPLAY DICTIONARY
print("CLASS", "\t", "SECTION", "\t", "STREAM")
for section in sectionsDictionary:
    sectionValue = sectionsDictionary[section]
    if(isinstance(sectionValue, list)):
        for d in range(0, len(sectionValue)):
            print("XI", "\t", section, "\t", sectionValue[d])
    else:
        print("XI", "\t", section, "\t", sectionValue)

# Q3
usingDict = dict()
simpleInit = {}

# Q2
# Syntax : 
# <dictionary name > = {key1: val1 , key2: val2 , key3: val3 , ...}
# example:
egDict = { "name": "world", "action": "Hello"}

# Q1
# The dictionary is an unordered collection that contains key:value pairs separated by commas inside curly brackets
