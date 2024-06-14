def sum_of_digits(n):

    total_sum = 0

    while n > 0:

        total_sum += n % 10

        n //= 10

    return total_sum

def digit_sum_upto(n):

    if n == 0:

        return 0

    result = 0

    current = 0

    place = 1

    while n // place > 0:

        lower_digits = n - (n // place) * place

        current_digit = (n // place) % 10

        higher_digits = n // (place * 10)

        result += higher_digits * place * 45

        result += current_digit * (current_digit - 1) // 2 * place

        result += current_digit * (lower_digits + 1)

        place *= 10

    return result

def digit_sum_range(L, U):

    return digit_sum_upto(U) - digit_sum_upto(L - 1)

L, U = map(int, input().split())

print(digit_sum_range(L, U))

