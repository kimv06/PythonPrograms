n=int(input("Enter the number: "))
t=n
count=0
while(t>0):
    t=t//10
    count=count+1
sum=0
t=n
b=0
while(t>0):
    b=t%10
    sum=sum+(b**count)
    t=t//10
if(sum==n):
    print("the number is armstrong")
else:
    print("the number is not armstrong")
