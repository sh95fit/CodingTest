def count_digits(n):
    count = [0] * 10
    factor = 1

    while n // factor > 0:
        lower = n - (n // factor) * factor
        curr = (n // factor) % 10
        higher = n // (factor * 10)

        for i in range(10):
            count[i] += higher * factor

        for i in range(curr):
            count[i] += factor

        count[curr] += lower + 1
        count[0] -= factor 
        factor *= 10

    return count

n = int(input())

result = count_digits(n)
print(" ".join(map(str, result)))

