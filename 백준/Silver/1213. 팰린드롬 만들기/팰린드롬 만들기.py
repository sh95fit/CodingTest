def create_palindrome(name):
    from collections import Counter    

    count = Counter(name)

    odd_char = None
    odd_count = 0

    for char, freq in count.items():
        if freq % 2 != 0:
            odd_char = char
            odd_count += 1
   
    if odd_count > 1:
        return "I'm Sorry Hansoo"

    half_palindrome = []

    for char in sorted(count.keys()):
        half_palindrome.append(char * (count[char] // 2))

    half_str = ''.join(half_palindrome)

    if odd_char:
        full_palindrome = half_str + odd_char + half_str[::-1]

    else:
        full_palindrome = half_str + half_str[::-1]

    return full_palindrome

name = input().strip()

print(create_palindrome(name))