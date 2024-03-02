S = input()
result = ''

for a in range(97,123):
    alphabet = chr(a)
    result += f"{S.find(alphabet)} "
    
print(result.strip())