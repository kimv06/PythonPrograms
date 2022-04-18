n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for k in range(1,n+1-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")
for i in range(1,n+1):
    for k in range(1,i+1):
        print(" ",end="")
    for j in range(1,n+1-i):
        print("*",end=" ")
    print("\n")
