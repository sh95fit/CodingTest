from itertools import permutations

def compute_lps(pattern):

    lps = [0] * len(pattern)

    length = 0

    i = 1

    while i < len(pattern):

        if pattern[i] == pattern[length]:

            length += 1

            lps[i] = length

            i += 1

        else:

            if length != 0:

                length = lps[length - 1]

            else:

                lps[i] = 0

                i += 1

    return lps

def kmp_search(text, pattern):

    lps = compute_lps(pattern)

    i = 0

    j = 0

    matches = 0

    while i < len(text):

        if pattern[j] == text[i]:

            i += 1

            j += 1

        if j == len(pattern):

            matches += 1

            j = lps[j - 1]

        elif i < len(text) and pattern[j] != text[i]:

            if j != 0:

                j = lps[j - 1]

            else:

                i += 1

    return matches

def is_magic_string(s, k):

    doubled_s = s + s

    return kmp_search(doubled_s[:-1], s) == k

def count_magic_permutations(strings, k):

    valid_count = 0

    for perm in permutations(strings):

        combined = ''.join(perm)

        if is_magic_string(combined, k):

            valid_count += 1

    return valid_count

N = int(input())

strings = [input().strip() for _ in range(N)]

K = int(input())

print(count_magic_permutations(strings, K))

