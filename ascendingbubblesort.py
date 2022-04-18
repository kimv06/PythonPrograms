n=int(input("Enter the number of elements to be taken: "))
L=[]
sum=0
for i in range(0,n):
    b=int(input("Enter the number: "))
    L.append(b)
print("BEFORE SORTING: ")
print(L)
for i in range(0,n-1):
    for j in range(0,n-1-i):
        if(L[j+1]<L[j]):
            t=L[j+1]
            L[j+1]=L[j]
            L[j]=t
    print("Elements after",i+1,"iteration: ")
    print(L)
print("After Sorting: ")
print(L)
