# Q5
stringInput = input("Enter a string: ").lower()
vowelDict = {"a":0,"e":0,"i":0,"o":0,"u":0}
for a in vowelDict:
    vowelDict[a] = stringInput.count(a)
    if(vowelDict[a] != 0):
        print(a, "occured", vowelDict[a], "times")

# Q4
# input country
nCountries = eval(input("Enter number of countries: "))
countryDictionary = {}
for b in range(0,nCountries):
    inputStatement = "Enter the "+ str(b+1)+" country"
    country = input(inputStatement).lower()
    capital = input("Enter its capital: ")
    currency = input("Enter its currency: ")
    countryNested = {"name": country, "capital": capital, "currency": currency}
    countryDictionary[country]= countryNested

# query using country:
countryQuery = input("Enter the country name: ").lower()
if(countryQuery in countryDictionary.keys()):
    countryInfo = countryDictionary[countryQuery]
    print("Name:",countryInfo["name"],"\t""Capital:",countryInfo["capital"],"\t""currency:",countryInfo["currency"])
else:
    print("no country found")

# display all countries
print("Country", "\t", "Capital", "\t", "Currency")
for c in countryDictionary:
    countryInfo = countryDictionary[c]
    print(countryInfo["name"],"\t",countryInfo["capital"],"\t",countryInfo["currency"])

# {country: {name: country , capital: capital, currency: currency}}

# Q3
nEmployees = eval(input("Enter the number of employees: "))
employDictionary = {}
for d in range(0, nEmployees):
    inputStatement = "Enter the "+ str(d+1)+" employ"
    employName = input(inputStatement)
    basicSalary = eval(input("Enter their basic salary: "))
    rentAllowance = eval(input("Enter their rent allowance: "))
    conveyanceAllowance = eval(input("Enter their conveyance allowance: "))
    totalSalary = basicSalary + rentAllowance+ conveyanceAllowance
    employNested = {"name": employName, "basicS": basicSalary, "rentAllowance": rentAllowance, "conveyanceAllowance": conveyanceAllowance, "TotalSalary": totalSalary}
    employDictionary[employName] = employNested

else:
    for e in employDictionary:
        employNested = employDictionary[e]
        print("Name:",employNested["name"],"\t""Total Salary", employNested["TotalSalary"])


# {employName: {name: employName, basicSalary: basicSalary, houseRentAllowance: houseRentAllowance , conveyanceAllowance: conveyanceAllowance, totalSalary: totalSalary}}

# Q2
nStrings = eval(input("Enter num words to sort: "))
chrDictionary = {}
for f in range(0, nStrings):
    inputStatement = "Enter the "+str(f+1)+" stirng: "
    stringEntered = input(inputStatement)
    key = stringEntered[0].lower()
    if(key not in chrDictionary):
        chrDictionary[key]= [stringEntered]
    else:
        stringList = chrDictionary[key]
        stringList.append(stringEntered)
        chrDictionary[key] = stringList

print(chrDictionary)

# {chr: [word1, word2.....]}

# Q1
nNames = eval(input("Enter number of people: "))
phoneDictionary = {}
for h in range(0, nNames):
    inputStatement = "Enter the "+str(h+1)+" persons name: "
    name = input(inputStatement)
    phoneNum = eval(input("Enter da phone number: "))
    phoneDictionary[name] = phoneNum

# query using name
query = input("Enter the name whose phone num you want to find: ")
if(query in phoneDictionary):
    print(query+"'s phone number is",phoneDictionary[query])
else:
    print("404")

# {name: phoneNum}