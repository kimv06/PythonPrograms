#convert decimal to binary
d=int(input("Enter the decimal num to convert: "))
b=0
i=0
while(d!=0):
    r=d%2
    b=b+r*(10**i)
    d=d//2
    i=i+1
print(b)
