charector = input("enter a charector").upper()

char_code = ord(charector)

if(char_code in range(48,58)):
    print("number")
elif(char_code in range(65,92)):
    if(char_code in ['A','E','I','O','U']):
        print("vowel")
    else:
        print("consonant")
else:
    print("special charector")