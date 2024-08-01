def find_kth_y(x, k):
    y = 0
    bit_position = 1 

    while k > 0:
        if x & bit_position == 0:  
            if k & 1:  
                y |= bit_position  

            k >>= 1

        bit_position <<= 1 

    return y

x, k = map(int, input().split())

print(find_kth_y(x, k))

