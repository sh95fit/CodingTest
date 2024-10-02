def find_lexicographically_smallest_word(word):
    n = len(word)
    smallest_word = None

    for i in range(1, n - 1):
        for j in range(i + 1, n):
            part1 = word[:i][::-1] 
            part2 = word[i:j][::-1]  
            part3 = word[j:][::-1]   

            new_word = part1 + part2 + part3

            if smallest_word is None or new_word < smallest_word:
                smallest_word = new_word

    return smallest_word

word = input().strip()

print(find_lexicographically_smallest_word(word))
