x,y=input().split()
N=int(x)
K=int(y)
L=input().split()
sum=0
for i in range (0,K,1):
  sum=sum+int(L[i])
print(sum)
