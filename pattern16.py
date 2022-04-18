n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for k in range(1,n+1-i):
        print(" ",end="")
    for j in range(1,i+1):
        if(j==1 or i==j or i==((n+1)//2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\n")
    
