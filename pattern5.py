n=int(input("Enter the number of rows: "))
for i in range(1,(n+1)):
    for k in range(i,n):
        print(" ",end=" ")
    for j in range(1,(i+1)):
        print("*",end=" ")
    print("\n")