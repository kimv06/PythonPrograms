n=int(input("Enter the number of elements to be taken: "))
L=[]
sum=0
for i in range(0,n):
    b=int(input("Enter the number: "))
    L.append(b)
print(L)
max1=L[0]
for i in range(0,n):
    if(L[i]>max1):
        max1=L[i]
print("The maximum element is: ",max1) 
