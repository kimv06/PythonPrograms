n=int(input("Enter the number of elements to be taken: "))
L=[]
sum=0
for i in range(0,n):
    b=int(input("Enter the number: "))
    L.append(b)
print(L)
print("The minimum element is: ",min(L)) 
