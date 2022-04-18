a=input("Enter a string: ")
b=input("Enter a string: ")
c=input("Enter a string: ")
for i in range(0,len(a)):
    if(a[i].isalpha()):
        if(a[i]=='A' or a[i]=='a' or a[i]=='E'or a[i]=='e'or a[i]=='I'or a[i]=='i'or a[i]=='O'or a[i]=='o'or a[i]=='U'or a[i]=='u'):
            a=a.replace(a[i],"*")
print("The updated first string: ",a)
for i in range(0,len(b)):
    if(b[i].isalpha()):
        if(b[i]!='A' and b[i]!='a' and b[i]!='E'and b[i]!='e'and b[i]!='I'and b[i]!='i'and b[i]!='O'and b[i]!='o'and b[i]!='U'and b[i]!='u'):
            b=b.replace(b[i],"$")
print("The updated second string: ",b)
for i in range(0,len(c)):
    if(c[i].isalpha()):
        if(c[i].isupper()==True):
            c=c.replace(c[i],c[i].lower())
print("The updated third string: ",c)
