def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
s=input("Enter the string: ")  
print ("The original string  is : ",end="")
print (s)  
if (s==reverse(s)):
    print("The string is palindrome")
else:
    print("The string is not palindrome")
    
