def find_next_element(N, sequence):
    is_arithmetic = True
    common_difference = sequence[1] - sequence[0]

    for i in range(1, N):
        if sequence[i] - sequence[i - 1] != common_difference:
            is_arithmetic = False

            break  

    if is_arithmetic:
        return sequence[-1] + common_difference

    is_geometric = True
    common_ratio = sequence[1] // sequence[0]

    for i in range(1, N):
        if sequence[i] // sequence[i - 1] != common_ratio:
            is_geometric = False

            break

    if is_geometric:
        return sequence[-1] * common_ratio

    return None

N = int(input())
sequence = [int(input()) for _ in range(N)]

next_element = find_next_element(N, sequence)
print(next_element)

