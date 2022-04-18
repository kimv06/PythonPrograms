def max(c,d):
    if(c>d):
        return c
    else:
        return d
a=int(input("Enter one num: "))
b=int(input("Enter one num: "))
c=int(input("Enter one num: "))
m=max(a,b)
print("The maximum of the first two numbers: ",m)
m1=max(m,c)
print("The maximum of all the numbers: ",m1)
