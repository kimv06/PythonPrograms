def gcd(c,d):
    if(d==0):
        return c
    else:
        return gcd(d,c%d)
a=int(input("Enter one num: "))
b=int(input("Enter one num: "))
c=int(input("Enter one num: "))
m=gcd(a,b)
print("The gcd of the first two numbers: ",m)
m1=gcd(m,c)
print("The gcd of all the numbers: ",m1)
