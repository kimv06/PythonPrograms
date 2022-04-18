n=int(input("Enter a number to check: "))
b=0
c=0
t=n
while(t>0):
    b=t%10
    c=(10*c)+b
    t=t//10
if(c==n):
    print("The number is palindrome.")
else:
    print("The number is not palindrome.")
