a=int(input("Enter a distinct number in a: "))
b=int(input("Enter another distinct number in b: "))
c=int(input("Enter one more distinct number in c: "))
if(a>b)and(a>c):
    print("a is maximum that is equal to : ",a)
elif(b>c):
    print("b is maximum that is equal to : ",b)
else:
    print("c is maximum that is equal to : ",c)
