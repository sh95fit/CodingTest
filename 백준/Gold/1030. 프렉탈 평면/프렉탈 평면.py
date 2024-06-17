def is_black(s, N, K, r, c):
    
    if s == 0:
        return 0

    segment_size = N ** (s - 1)
    start_black = (N - K) // 2 * segment_size
    end_black = start_black + K * segment_size

    if start_black <= r % (N * segment_size) < end_black and start_black <= c % (N * segment_size) < end_black:
        return 1
    else:
        return is_black(s - 1, N, K, r % segment_size, c % segment_size)

def fractal(s, N, K, R1, R2, C1, C2):

    result = []

    for r in range(R1, R2 + 1):
        row = []
        for c in range(C1, C2 + 1):
            row.append(is_black(s, N, K, r, c))
        result.append("".join(map(str, row)))
    return result

s, N, K, R1, R2, C1, C2 = map(int, input().split())

result = fractal(s, N, K, R1, R2, C1, C2)

for line in result:
    print(line)

