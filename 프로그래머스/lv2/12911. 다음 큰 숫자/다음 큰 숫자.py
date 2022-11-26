def solution(n):
    std = n
    while True :
        n += 1
        if n > std and bin(std).count('1') == bin(n).count('1') :
            break
    return n