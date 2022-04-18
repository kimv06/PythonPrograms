r=int(input("Enter the no. of rows: "))
c=int(input("Enter the no. of columns: "))
mat1=[]
print("Enter the elements of first matrix: ")
for i in range(0,r):
    a=[]
    for j in range(0,c):
        b=int(input("Enter a no.: "))
        a.append(b)
    mat1.append(a)
print("The elements of first matrix: ")
for i in range(0,r):
    for j in range(0,c):
              print(mat1[i][j],end=" ")
    print("\n")
mat2=[]
print("Enter the elements of second matrix: ")
for i in range(0,r):
    t=[]
    for j in range(0,c):
        d=int(input("Enter a no.: "))
        t.append(d)
    mat2.append(t)
print("The elements of second matrix: ")
for i in range(0,r):
    for j in range(0,c):
              print(mat2[i][j],end=" ")
    print("\n")
S=[]
for i in range(0,r):
    e=[]
    for j in range(0,c):
        f=mat1[i][j]+mat2[i][j]
        e.append(f)
    S.append(e)
print("The added matrix: ")
for i in range(0,r):
    for j in range(0,c):
              print(S[i][j],end=" ")
    print("\n")        
                     
