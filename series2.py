n=int(input("Enter the number of terms: "))
for x in range(0,91,15):
    x1=(3.14285*x)/180
    s=0
    k=0
    for i in range(1,n+1,2):
        p=x1**i
        f=1
        for j in range(1,i+1):
            f=f*j
        term=((-1)**k)*(p/f)
        k+=1
        s=s+term
    print("sin",x,"=",s)
    
