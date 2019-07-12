n=int(input())
s=list(map(int,input().split()))
b=[]
for i in range(n):
    if s[i]==i:
        b.append(i)
        b.sort()
if(len(b)==0):
    print("-1")
else:
    print(" ".join(map(str,b)))
    
