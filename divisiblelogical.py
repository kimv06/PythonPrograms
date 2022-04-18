n=int(input("Enter a number : "))
if(n%4==0)and(n%7==0):
        print("Number is divisible by both 4 and 7.")
elif(n%4==0):
    print("Number is divisible by 4 but not divisible by 7.")
elif(n%7==0):
    print("Number is divisible by 7 but not divisible by 4.")
else:
    print("Number is neither divisible by 7 nor divisible by 4.") 
