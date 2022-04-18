r1=int(input("Enter the no. of rows of first matrix: "))
c1=int(input("Enter the no. of columns of first matrix: "))
r2=int(input("Enter the no. of rows of second matrix: "))
c2=int(input("Enter the no. of columns of second matrix: "))
if(c1==r2):
    mat1=[]
    print("Enter the elements of first matrix: ")
    for i in range(0,r1):
        a=[]
        for j in range(0,c1):
            b=int(input("Enter a no.: "))
            a.append(b)
        mat1.append(a)
    print("The elements of first matrix: ")
    for i in range(0,r1):
        for j in range(0,c1):
                  print(mat1[i][j],end=" ")
        print("\n")
    mat2=[]
    print("Enter the elements of second matrix: ")
    for i in range(0,r2):
        t=[]
        for j in range(0,c2):
            d=int(input("Enter a no.: "))
            t.append(d)
        mat2.append(t)
    print("The elements of second matrix: ")
    for i in range(0,r2):
        for j in range(0,c2):
                  print(mat2[i][j],end=" ")
        print("\n")
    S=[]
    for i in range(0,r1):
        e=[]
        for j in range(0,c2):
            f=0
            e.append(f)
        S.append(e)
    for i in range(0,r1):
       for j in range(0,c2):
           for k in range(0,c1):
               S[i][j]+=mat1[i][k]*mat2[k][j]
    print("The multiplied matrix: ")
    for i in range(0,r1):
        for j in range(0,c2):
                  print(S[i][j],end=" ")
        print("\n")        
else:
    print("The condition of multiplication of matrices is not satisfied.")
