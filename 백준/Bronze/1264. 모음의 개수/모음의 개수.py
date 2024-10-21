def count_vowels(line):
    vowels = 'aeiouAEIOU'  
    count = sum(1 for char in line if char in vowels)  # Count vowels using a generator expression

    return count

while True:
    line = input()  

    if line == '#':  
        break  

    print(count_vowels(line))  

