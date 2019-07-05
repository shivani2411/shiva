def sh(p,a):
  if(len(p)==len(a)):
    return("yes")
  else:
   return("no")
p,a=map(str,input().split())
print(sh(p,a))
