n=int(input("Enter the number of elements to be taken: "))
L=[]
sum=0
for i in range(0,n):
    b=int(input("Enter the number: "))
    L.append(b)
for i in range(0,n):
    if(L[i]%2==0):
        sum=sum+L[i]
print(L)
print("The sum of the even elements: ",sum)
