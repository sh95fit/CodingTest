def decimal_to_base(n, base):
    result = ""
    while n > 0:
        remainder = n % base
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(remainder + ord('A') - 10) + result
        n //= base
    return result if result else "0"

N, B = map(int, input().split())

result = decimal_to_base(N, B)
print(result)
