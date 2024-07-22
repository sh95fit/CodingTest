def min_swaps_to_group_a(s):
    n = len(s)
    count_a = s.count('a')

    if count_a == n or count_a == 0:
        return 0

    double_s = s + s
    min_swaps = float('inf')
    current_non_a_count = 0

    for i in range(count_a):
        if double_s[i] != 'a':
            current_non_a_count += 1

    min_swaps = min(min_swaps, current_non_a_count)

    for i in range(count_a, 2 * n):
        if double_s[i] != 'a':
            current_non_a_count += 1

        if double_s[i - count_a] != 'a':
            current_non_a_count -= 1

        min_swaps = min(min_swaps, current_non_a_count)

    return min_swaps

s = input().strip()

print(min_swaps_to_group_a(s))

