c=input()
c=c.lower()
if c in ['a','e','i','o','u']:
    print("Vowel")
elif ord(c) in range(97,123):
    print("Consonant")
else:
    print("Invalid")
    
