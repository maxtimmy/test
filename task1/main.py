n,m=map(int,input().split())
s=(2*m-1)%n
i=0
r=''
for _ in range(n):
    r+=str(i+1)
    i=(i+s)%n+1
print(r)
