subject_marks = eval(input("Enter marks: "))

if(subject_marks >=91 and subject_marks <= 100):
    print("A1")
elif(subject_marks >=81 and subject_marks <= 90):
    print("A2")
elif(subject_marks >=71 and subject_marks <= 80):
    print("B1")
elif(subject_marks >=61 and subject_marks <= 70):
    print("B2")
elif(subject_marks >=51 and subject_marks <= 60):
    print("C1")
elif(subject_marks >=41 and subject_marks <= 50):
    print("C2")
elif(subject_marks >=33 and subject_marks <= 40):
    print("D")
elif(subject_marks >=0 and subject_marks < 33):
    print("E")
else:
    print("enter valid marks")