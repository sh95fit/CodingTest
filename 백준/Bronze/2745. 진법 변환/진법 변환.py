def base_to_decimal(n, base):
    decimal = 0
    power = len(n) - 1
    
    for digit in n:
        if digit.isdigit():
            digit_value = int(digit)
        else:
            digit_value = ord(digit) - ord('A') + 10
        decimal += digit_value * (base ** power)
        power -= 1
    
    return decimal

N, B = input().split()
B = int(B)

result = base_to_decimal(N, B)
print(result)
