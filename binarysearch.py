n=int(input("Enter the number of elements of list: "))
L=[]
for i in range(0,n):
    b=int(input("Enter the number: "))
    L.append(b)
print(L)
s=int(input("Enter the search element: "))
lb=0
ub=n-1
flag=0
count=0
while(lb<=ub):
    mid=(lb+ub)//2
    count+=1
    if(L[mid]==s):
        flag=1
        break
    elif(s<L[mid]):
        ub=mid-1
    else:
        lb=mid+1
if(flag==0):
    print("THE ELEMENT IS NOT PRESENT.")
else:
    print("THE ELEMENT IS PRESENT.")
    print("THE INDEX NUMBER IS:",mid)
print("THE NUMBER OF SEARCHES = ",count)
