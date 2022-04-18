n=int(input("Enter the number: "))
i=1
temp=1
if(n<0):
    print("Invalid Input")
else:
    while(i<=n):
        temp=temp*i
        i=i+1
    print("The factorial of the number: ",temp)
