def leapYearDeterminer(sampleYear):  # finding if year is leap year or not
    if sampleYear % 4 == 0:
        if sampleYear % 100 == 0:
            if sampleYear % 400 == 0:
                return "Leap year"
            else:
                return "Not Leap year"
        else:
            return "Leap year"
    else:
        return "Not Leap year"


todayDate = input("Enter Today's Date:(DD/MM/YY): ")  # inputting the date in dd/mm/yy form..
dateSplitList = todayDate.split("/")  # splitting the entered date at / and feeding it to list
monthHaving30Days = ["4", "6", "9", "11"]  # month number having 30 days
monthHaving28Days = ["2"]  # month number having 28/29 days
leapYear = leapYearDeterminer(int(dateSplitList[2]))  # running leap year function and saving output to Leap Year
dateSplitConvertedList = []  # initializing blank list to store the split dates and months after all parameters are met..
if dateSplitList[0] == "30" and dateSplitList[1] in monthHaving30Days:  # case of date being 30
    term1 = 1
    term2 = int(dateSplitList[1]) + 1
    dateSplitConvertedList.append(term1)
    dateSplitConvertedList.append(term2)
elif dateSplitList[0] == "31" and dateSplitList[1] not in monthHaving30Days and dateSplitList[1] not in monthHaving28Days:
    # case of date being 31.
    term1 = 1
    term2 = int(dateSplitList[1]) + 1
    dateSplitConvertedList.append(term1)
    dateSplitConvertedList.append(term2)
elif dateSplitList[0] == "28" or dateSplitList[0] == "29" and dateSplitList[1] in monthHaving28Days:  # case of date being 28 or 29
    if leapYear == "Not Leap year":  # if year is not leap year
        term1 = 1
        term2 = int(dateSplitList[1]) + 1
        dateSplitConvertedList.append(term1)
        dateSplitConvertedList.append(term2)
    else:
        if dateSplitList[0] == "28":  # if year is leap year and 28 entered..
            term1 = 29
            term2 = int(dateSplitList[1])
            dateSplitConvertedList.append(term1)
            dateSplitConvertedList.append(term2)
        else:  # if year is leap year and 29 entered..
            term1 = 1
            term2 = int(dateSplitList[1]) + 1
            dateSplitConvertedList.append(term1)
            dateSplitConvertedList.append(term2)
else:  # case of normal date..
    term1 = int(dateSplitList[0]) + 1
    dateSplitConvertedList.append(term1)
    dateSplitConvertedList.append(dateSplitList[1])

if str(dateSplitConvertedList[1]) not in monthHaving30Days and str(dateSplitConvertedList[1]) not in monthHaving28Days:
    # case when month has 31 days
    daysLeft = 31 - dateSplitConvertedList[0]
    print("Days left after Tomorrow are", daysLeft)
elif str(dateSplitConvertedList[1]) in monthHaving28Days:  # case when month has 28 days
    if leapYear == "Not Leap year":  # case if not leap year
        daysLeft = 28 - dateSplitConvertedList[0]
        print("Days left after Tomorrow are", daysLeft)
    else:  # case if leap year.
        daysLeft = 29 - dateSplitConvertedList[0]
        print("Days left after Tomorrow are", daysLeft)
else: # case when month has 30 days..
    daysLeft = 30 - dateSplitConvertedList[0]
    print("Days left after Tomorrow are", daysLeft)
