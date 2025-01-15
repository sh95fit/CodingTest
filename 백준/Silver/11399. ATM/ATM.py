import sys
input = sys.stdin.readline

N = int(input().strip())

hlist = list(map(int, input().strip().split()))

# 버블 정렬
# swap_count = 0

# for _ in range(N):
#     for i in range(N-1):
#         if hlist[i] > hlist[i+1]:
#             hlist[i], hlist[i+1] = hlist[i+1], hlist[i]
#             swap_count += 1

#     if swap_count == 0:
#         break

# 선택 정렬 (최대값을 찾아 정렬)
# for i in range(N-1, 0, -1):
#     max_index = 0
#     for j in range(1, i+1):
#         if hlist[j] > hlist[max_index]:
#             max_index = j

#     hlist[i], hlist[max_index] = hlist[max_index], hlist[i]

# 선택 정렬 (최솟값을 찾아 정렬)
# for i in range(N-1):
#     min_index = i
#     for j in range(i+1, N):
#         if hlist[j] < hlist[min_index]:
#             min_index = j

#     if i != min_index:
#         hlist[i], hlist[min_index] = hlist[min_index], hlist[i]

# 삽입 정렬
for i in range(1, N):
    key = hlist[i]
    j = i - 1

    while j >= 0 and hlist[j] > key:
        hlist[j+1] = hlist[j]
        # print(f"while ==> {hlist}")
        j -= 1

    hlist[j+1] = key

    # print(f"for ==> {hlist}")

prefix_sum = [0]*(N+1)
for i in range(1, N+1):
    prefix_sum[i] = hlist[i-1] + prefix_sum[i-1]

print(sum(prefix_sum))