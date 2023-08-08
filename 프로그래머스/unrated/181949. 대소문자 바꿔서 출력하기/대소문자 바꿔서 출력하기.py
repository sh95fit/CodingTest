str = list(input())

for i, s in enumerate(str) :
    if s.isupper() :
        str[i]=s.lower()
    else :
        str[i]=s.upper()

print(''.join(str))