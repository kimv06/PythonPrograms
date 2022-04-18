#question 4(a):
n=int(input("Enter the no. of elements to be taken: "))
L=[]
sum=0
for i in range(0,n):
    b=int(input("Enter a number: "))
    L.append(b)
print(L)
for i in range(0,n):
    if(L[i]%2==0):
        sum=sum+L[i]
print("The sum of the even elements in the list = ",sum)
