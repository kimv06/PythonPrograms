n=input("Enter a string: ")
a=0
d=0
s=0
c=0
for i in range(0,len(n)):
    if(n[i].isalpha()):
        a+=1
    elif(n[i].isdigit()):
        d+=1
    elif(n[i].isspace()):
        s+=1
    else:
        c+=1
print("The numbers of alphabets: ",a)
print("The numbers of digits: ",d)
print("The numbers of spaces: ",s)
print("The numbers of special characters: ",c)
