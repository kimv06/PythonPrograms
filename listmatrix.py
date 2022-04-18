#take some values as input and print the numbers in matrix format
r=int(input("Enter the number of rows: "))
c=int(input("Enter the number of columns: "))
mat1=[]
for i in range(0,r):
    a=[]
    for j in range(0,c):
        b=int(input("Enter the number of matrix: "))
        a.append(b)
    mat1.append(a)
for i in range(0,r):
    for j in range(0,c):
        print(mat1[i][j],end=" ")
    print("\n")
    
              
      
