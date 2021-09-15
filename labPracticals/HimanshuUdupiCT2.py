print("Name", "Himanshu Udupi")
print("Class", "XI B")
print("Roll No", "11", sep=":")
print("--------------------------------------------------------------------")
# Question 1
for a in range(51, 60, 2):
    termToDisplayed = a + 1
    print(termToDisplayed)

# Question 2
# Empty for loop can be used to delay the runtime of the program, it can also be used to update the value of the variable used in the for loop.

# Question 3
# Difference Between for and while Loop : While loop is a entry controlled loop. For loop is an iteration loop and has only range.
# Similarities both of them are conditional statements and help perform a same task many times.

# Question 4
# Right - printed until computer crashes

# Question 5
# A: If the entry condition is false the loop will not execute even once
# B: One time

# Question 6
b = 1
while b < 6:
    print("Cube of", b, "is", b ** 3)
    b += 1

# Question 7
fibonacciList = [0, 1]
noOfTerms = eval(input("Enter number of terms in sequence: "))
if noOfTerms > 2:
    limitOfRange = noOfTerms - 2
    for c in range(0, limitOfRange):
        nthTerm = fibonacciList[c] + fibonacciList[c + 1]
        fibonacciList.append(nthTerm)
    print(*fibonacciList)
else:
    if noOfTerms == 2:
        print(*fibonacciList)
    else:
        print(fibonacciList[0])

# Question 8
# a) T + w + i + n + k + l + e +
# b)
#       1
#       2
#       3
#       4
#       5
#       6
#       7
#       8
#       9
#       10
# c)
#       20
#       16

# d)
#       10
#       11
#       12
#       13
#       14

# Question 9
# Break statement is used to break the flow of a program usually used in loops.
# Continue statement is used when the programmer doesnt know what to write in a block of code which is necessary.
# Continue statement does not break the flow of program.

# Question 10
number = input("Enter number above 1000: ")
reversedNum = ""
for d in range(-1, -len(number) - 1, -1):
    term = number[d]
    reversedNum += term
else:
    print(reversedNum)
