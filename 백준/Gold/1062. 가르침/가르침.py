from itertools import combinations

def count_readable_words(words, selected_letters):
    readable_count = 0
    for word in words:
        is_readable = True
        for char in word:
            if not selected_letters[ord(char) - ord('a')]:
                is_readable = False
                break
        if is_readable:
            readable_count += 1
    return readable_count

def main():
    N, K = map(int, input().split())
    words = [input()[4:-4] for _ in range(N)] 

    must_learn = {'a', 'n', 't', 'i', 'c'}

    if K < 5:
        print(0)
        return

    if K == 26:
        print(N)
        return

    remaining_letters = set()
    for word in words:
        remaining_letters.update(set(word) - must_learn)

    possible_letters = list(remaining_letters)

    max_readable = 0
    for letters in combinations(possible_letters, min(K-5, len(possible_letters))):
        selected_letters = [False] * 26
        for letter in must_learn:
            selected_letters[ord(letter) - ord('a')] = True
        for letter in letters:
            selected_letters[ord(letter) - ord('a')] = True
        max_readable = max(max_readable, count_readable_words(words, selected_letters))
    
    print(max_readable)

if __name__ == "__main__":
    main()
