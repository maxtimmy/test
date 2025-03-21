f=open("file1.txt")
x,y=map(float,f.readline().split())
r=float(f.readline())
f.close()
g=open("file2.txt")
for l in g:
 a,b=map(float,l.split())
 d=((a-x)**2+(b-y)**2)**0.5
 if abs(d-r)<1e-9:print(0)
 elif d<r:print(1)
 else:print(2)
g.close()
