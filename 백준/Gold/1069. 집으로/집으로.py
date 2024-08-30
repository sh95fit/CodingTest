import math

X, Y, D, T = map(int, input().split())

dist = math.sqrt(X ** 2 + Y ** 2)
min_time = dist

if D > dist:
    min_time = min(min_time, T + D - dist, 2 * T)  # 점프 후 걷기와, 점프-반점프

else:
    jumps_needed = dist // D
    remaining_dist = dist - jumps_needed * D
    min_time = min(min_time, jumps_needed * T + remaining_dist)
    min_time = min(min_time, (jumps_needed + 1) * T)

print(f"{min_time:.9f}")

