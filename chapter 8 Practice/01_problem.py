
def greatest(a,b,c):
  if(a>b and a>c):
    return a
  elif(b>a and b>c):
    return b
  elif(c>a and c>b):
    return c
  
  # a =int(input("Enter the number: "))
  # b= int(input("Enter the number: "))
  # c= int(input("Enter the number: "))
a=4
b=21
c=12
  
print(greatest(a,b,c))