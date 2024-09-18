def get_pattern(word):

    """ Returns a string representing the pattern of the given word. """

    char_map = {}

    pattern = []

    next_index = 0

    for char in word:

        if char not in char_map:

            char_map[char] = next_index

            next_index += 1

        pattern.append(str(char_map[char]))

    return ''.join(pattern)

def count_similar_pairs(words):

    pattern_count = {}

    

    # Generate patterns for all words and count their occurrences

    for word in words:

        pattern = get_pattern(word)

        if pattern not in pattern_count:

            pattern_count[pattern] = 0

        pattern_count[pattern] += 1

    

    # Calculate the number of similar pairs

    similar_pairs = 0

    for count in pattern_count.values():

        if count > 1:

            similar_pairs += count * (count - 1) // 2  # C(count, 2)

    

    return similar_pairs

# Read input

N = int(input().strip())

words = [input().strip() for _ in range(N)]

# Get the result

result = count_similar_pairs(words)

# Print the output

print(result)

