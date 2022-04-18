n=int(input("Enter a number: "))
i=0
temp=1
if(n<=0):
    print("Invalid Input")
else:
    for i in range(1,n+1):
        temp=temp*i
    print("The factorial of the number: ",temp) 
