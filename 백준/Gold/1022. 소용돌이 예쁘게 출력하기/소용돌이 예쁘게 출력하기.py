def find_value_at_position(r, c):
    k = max(abs(r), abs(c))
    max_num = (2 * k + 1) ** 2
    
    if r == k:
        return max_num - (k - c)
    elif c == -k:
        return max_num - (2 * k + (k - r))
    elif r == -k:
        return max_num - (4 * k + (k + c))
    elif c == k:
        return max_num - (6 * k + (k + r))

def generate_spiral(r1, c1, r2, c2):
    spiral_map = []
    max_value = 0
    
    for r in range(r1, r2 + 1):
        row = []
        for c in range(c1, c2 + 1):
            value = find_value_at_position(r, c)
            row.append(value)
            max_value = max(max_value, value)
        spiral_map.append(row)

    max_width = len(str(max_value))
    
    for row in spiral_map:
        print(" ".join(f"{x:>{max_width}}" for x in row))

r1, c1, r2, c2 = map(int, input().split())

generate_spiral(r1, c1, r2, c2)

