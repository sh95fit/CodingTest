word = input()
croatian_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
i = 0

while i < len(word):
    if word[i:i+2] in croatian_alphabets:
        count += 1
        i += 2
    elif word[i:i+3] in croatian_alphabets:
        count += 1
        i += 3
    else:
        count += 1
        i += 1

print(count)
