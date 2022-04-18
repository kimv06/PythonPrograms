n=int(input("Enter the value of n: "))
c=0
if(n>1):
    for i in range(2,n//2+1):
        if(n%i==0):
            print("The number is not prime.")
            break
        else:
            print("The number is prime")
else:
    ("The number is not prime.")
