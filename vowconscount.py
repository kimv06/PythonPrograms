n=input("Enter a string: ")
v=0
c=0
i=0
for i in range(0,len(n)):
    if(n[i].isalpha()):
        if(n[i]=='A' or n[i]=='a' or n[i]=='E'or n[i]=='e'or n[i]=='I'or n[i]=='i'or n[i]=='O'or n[i]=='o'or n[i]=='U'or n[i]=='u'):
            v+=1
        else:
            c+=1
print("The no. of vowels: ",v)
print("The no. of consonents: ",c)
