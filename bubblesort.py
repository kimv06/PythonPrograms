l1=[]
k=0
n=int(input("Enter the number of elements: "))
for i in range(0,n):
    k=int(input("Enter a number: "))
    l1.append(k)
print("Before Sorting:")
print(l1)
for i in range(0,len(l1)-1):
    for j in range(0,len(l1)-1-i):
        t=0
        if(l1[j]>l1[j+1]):
            t=l1[j]
            l1[j]=l1[j+1]
            l1[j+1]=t
print("After Sorting:")
print(l1)
