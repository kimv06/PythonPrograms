def fact(i):
    if i==1:
        return 1
    else:
        return i*fact(i-1)
x = int(input("Enter a number: "))
n=int(input("Enter the no. of terms: "))
sum=1
for i in range(1,n+1):
    sum=sum+pow(x,i)/fact(i)
print("The exponential value of",x,"upto",n,"terms is:",sum)
