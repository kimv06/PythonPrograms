#print the following series:0,2,1,3,1,5,2,7,3,11,5,13,8,17,13,19,21,23,34
n=int(input("Enter the no. of terms: "))
if(n%2==0):
    n1=n//2
    n2=n//2
else:
    n1=(n+1)//2
    n2=(n-1)//2
P=[]
F=[]
t1=0
t2=1
i=0
F.append(t1)
F.append(t2)
while(i<(n1-2)):
    s=t1+t2
    F.append(s)
    t1=t2
    t2=s
    i+=1
print(F)
i=2
countp=1
while(countp<=(n2//2)):
    flag=1
    for j in range(2,(i//2+1)):
        if(i%j==0):
            flag=0
            break 
    if(flag==1):
        P.append(i)
        countp=countp+1
    i=i+1
print(P)
total=[]
k=0
even=0
odd=0
for k in range(0,n):
    if(k%2==0):
        total.append(F[even])
        even+=1
    else:
        total.append(P[odd])
        odd+=1
print(total)
        
                   
