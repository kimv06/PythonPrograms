n=int(input("Enter the number of elements to be taken: "))
L=[]
sum=0
for i in range(0,n):
    b=int(input("Enter the number: "))
    L.append(b)
print(L)
min1=L[0]
for i in range(0,n):
    if(L[i]<min1):
        min1=L[i]
print("The minimum element is: ",min1) 
