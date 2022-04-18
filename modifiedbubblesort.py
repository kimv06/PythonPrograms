n=int(input("enter the num of ele of list"))
L1=[]
for i in range(0,n):
    b=int(input("enter num"))
    L1.append(b)
print(L1)
for i in range(0,n):
    for j in range(0,n-1-i):
        swap=0
        temp=0
        if(L1[j+1]<L1[j]):
            temp=L1[j+1]
            L1[j+1]=L1[j]
            L1[j]=temp
            swap+=1
    if(swap==0):
        break
print(L1)
