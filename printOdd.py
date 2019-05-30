x,y=input().split()
num1=int(x)
num2=int(y)
if(num1%2==0):
  num1=num1+1
else:
  num1=num1+2
for i in range(num1,num2,+2):
  print(i)
