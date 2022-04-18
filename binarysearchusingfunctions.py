def binarysearch(lb,ub,s):
    flag=0
    index=0
    while(lb<=ub):
        mid=(lb+ub)//2
        if(L[mid]==s):
            flag=1
            index=mid
            break
        elif(s<L[mid]):
            ub=mid-1
        else:
            lb=mid+1
    if(flag==1):
        return index
    else:
        return -1
n=int(input("Enter the number of elements of list: "))
L=[]
for i in range(0,n):
    b=int(input("Enter the number: "))
    L.append(b)
print(L)
s=int(input("Enter the search element: "))
a=binarysearch(0,(n-1),s)
if(a!=-1):
    print("THE ELEMENT IS PRESENT.")
    print("THE INDEX NUMBER IS:",a)
else:
    print("THE ELEMENT IS NOT PRESENT.")

