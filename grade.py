marks=int(input("Enter the total marks of the student: "))
if(marks>100):
    print("INVALID INPUT.")
elif(marks>=90):
    if(marks<=100):
        print("Grade is Outstanding.")
elif(marks>=80):
    if(marks<=89):
        print("Grade is Excellent.")
elif(marks>=70):
    if(marks<=79):
        print("Grade is Fine.")
elif(marks>=60):
    if(marks<=69):
        print("Grade is Good.")
elif(marks>=50):
    if(marks<=59):
        print("Grade is Average.")
elif(marks>=40):
    if(marks<=49):
        print("Grade is Just Pass.")
elif(marks>=0):
    if(marks<=39):
        print("FAIL.")
else:
    print("INVALID INPUT.")
