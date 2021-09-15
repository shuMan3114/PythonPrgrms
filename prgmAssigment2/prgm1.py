#  Using For LOOP to input and multiply( repeating code is not efficient )
output = 1
for i in range(1,4):
    term = eval(input("Enter the "+ str(i) +" number: ")) #Inputing the numbers
    output= output*term #multiplying the input to the output..

print(output)
