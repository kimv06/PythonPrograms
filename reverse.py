n=int(input("Enter the number; "))
i=0
b=0
c=0
while(i<n):
    b=n%10
    c=b+(10*c)
    n=n//10
print("The reverse of the number is: ",c)
