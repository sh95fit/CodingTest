def minimum_boxes_needed(n, m, weights):
    if n == 0:
        return 0

    current_box_weight = 0
    box_count = 1

    for weight in weights:
        if current_box_weight + weight <= m:
            current_box_weight += weight
        else:
            box_count += 1
            current_box_weight = weight

    return box_count

n, m = map(int, input().split())

if n > 0:
    weights = list(map(int, input().split()))

else:
    weights = []

print(minimum_boxes_needed(n, m, weights))

