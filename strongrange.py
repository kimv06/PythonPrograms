def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
def is_strong(n):
    if n<0:
        return False
    number_copy=n
    strong_sum=0
    while n:
        remainder=n%10
        strong_sum+=fact(remainder)
        n//=10
    return strong_sum==number_copy
min_value=int(input('Enter minimum value: '))
max_value=int(input('Enter maximum value: '))
print("Strong numbers between the range are: ")
for i in range(min_value, max_value+1):
    if is_strong(i):
        print(i, end=' ')
