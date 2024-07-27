def most_frequent_sum(S1, S2, S3):
    from collections import defaultdict

    frequency = defaultdict(int)

    for i in range(1, S1 + 1):
        for j in range(1, S2 + 1):
            for k in range(1, S3 + 1):
                total_sum = i + j + k
                frequency[total_sum] += 1

    max_frequency = 0
    most_frequent_sum = 0

    for total_sum in sorted(frequency.keys()):
        if frequency[total_sum] > max_frequency:
            max_frequency = frequency[total_sum]
            most_frequent_sum = total_sum

    return most_frequent_sum

S1, S2, S3 = map(int, input().split())

print(most_frequent_sum(S1, S2, S3))

