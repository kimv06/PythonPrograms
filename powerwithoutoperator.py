def power(a,b):
    r=1
    for i in range(b):
        r*=a
    return r
n1=int(input("Enter a number: "))
n2=int(input("Enter the power: "))
x=power(n1,n2)
print("the answer =",x)
