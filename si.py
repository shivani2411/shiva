inp=input()
strei=str(input())
vowels=('a','e','i','o','u')
for x in strei:
    if x in vowels:
        strei=strei.replace(x,"")
print(strei[::-1])
