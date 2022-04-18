def max(c,d):
    if(c>d):
        return c
    else:
        return d
n=int(input("Enter the number of elements to be taken: "))
L=[]
sum=0
for i in range(0,n):
    b=int(input("Enter the number: "))
    L.append(b)
print(L)
m=L[0]
for i in range(1,n):
    m=max(m,L[i])
print("The maximum of all the numbers: ",m)
