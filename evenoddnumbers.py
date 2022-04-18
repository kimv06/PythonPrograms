n=int(input("Enter the value of n: "))
print("The 1st",n,"even numbers are: ")
for i in range(2,2*n,2):
    print(i)
print("The 1st",n,"odd numbers are: ")
for i in range(1,2*n,2):
    print(i)

