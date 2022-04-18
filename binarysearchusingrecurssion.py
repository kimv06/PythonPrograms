def binarysearch(lb,ub,s):
    mid=(lb+ub)//2
    if(lb>ub):
        return -1
    if(L[mid]==s):
        return mid
    elif(s<L[mid]):
        return binarysearch(lb,mid-1,s)
    else:
        return binarysearch(mid+1,ub,s)
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

