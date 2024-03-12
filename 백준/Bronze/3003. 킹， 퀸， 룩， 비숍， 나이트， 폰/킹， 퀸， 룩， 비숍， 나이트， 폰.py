#white_pieces = list(map(int, input().split()))

#correct_pieces = [1, 1, 2, 2, 2, 8]

#result = [correct - white for correct, white in zip(correct_pieces, white_pieces)]
#print(*result)

original = list(map(int, input().split()))
real = [1, 1, 2, 2, 2, 8]
res = []

for i, o in enumerate(original):
    res.append(real[i] - o)

print(*res)
        