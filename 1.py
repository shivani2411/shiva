from itertools import combinations
a,k=map(int,input().split())
ab=len(str(a))
1st=list(combinations(str(a),ab-k))
1st=sorted(1st)
print(*1st[0],sep='')
