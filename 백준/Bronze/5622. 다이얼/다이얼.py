def calculate_dial_time(char):
    dial_dict = {
        'A': 2, 'B': 2, 'C': 2,
        'D': 3, 'E': 3, 'F': 3,
        'G': 4, 'H': 4, 'I': 4,
        'J': 5, 'K': 5, 'L': 5,
        'M': 6, 'N': 6, 'O': 6,
        'P': 7, 'Q': 7, 'R': 7, 'S': 7,
        'T': 8, 'U': 8, 'V': 8,
        'W': 9, 'X': 9, 'Y': 9, 'Z': 9
    }
    return dial_dict[char]

def calculate_total_time(word):
    total_time = 0
    for char in word:
        total_time += calculate_dial_time(char)
    return total_time + len(word)

if __name__ == "__main__":
    word = input().strip()
    result = calculate_total_time(word)
    print(result)