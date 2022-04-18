#convert binary to decimal
b=0
c=0
d=0
n=int(input("Enter the binary number : "))
while(n>0):
    b=n%10
    n=n//10
    d=d+(b*2**c)
    c=c+1
print(d)
