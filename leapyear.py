n=int(input("Enter a year number: "))
if ((n%4==0) and (n%400==0) or (n%100 !=0)):
    print("The year is Leap Year.")
else:
    print("The year is not Leap Year.")
