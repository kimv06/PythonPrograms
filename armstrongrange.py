s=int(input("Enter lower range: "))
e=int(input("Enter upper range: "))  
for n in range(s,e+1):
   order=len(str(n))
   sum=0  
   temp=n  
   while(temp>0):  
       digit=temp%10  
       sum+=digit**order  
       temp//=10  
   if(n==sum):
      print(n)
