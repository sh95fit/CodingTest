def max_lit_rows_after_switches(lamps, K):

    from collections import Counter

    

    N = len(lamps)

    M = len(lamps[0])

    

    row_count = Counter()

    for row in lamps:

        row_tuple = tuple(row)

        row_count[row_tuple] += 1

    

    max_lit_rows = 0

    

    for row, count in row_count.items():

        zero_count = row.count(0)

        

        if zero_count <= K and (K - zero_count) % 2 == 0:

            max_lit_rows = max(max_lit_rows, count)

    

    return max_lit_rows

N, M = map(int, input().split())

lamps = [list(map(int, input().strip())) for _ in range(N)]

K = int(input().strip())

print(max_lit_rows_after_switches(lamps, K))

