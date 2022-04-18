n=int(input("Enter the number of elements of list: "))
L=[]
index=0
for i in range(0,n):
    b=int(input("Enter the number: "))
    L.append(b)
print(L)
s=int(input("Enter the search element: "))
for i in range(0,n):
    if(L[i]==s):
        index=i
        break
    else:
        i=i+1
if(i!=n):
    print("The element is present.")
    print("The index is=",index)
else:
    print("The element is not present.")
