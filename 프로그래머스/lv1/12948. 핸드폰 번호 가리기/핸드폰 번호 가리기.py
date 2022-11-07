def solution(phone_number):
    num = list(phone_number)
    for i in range(len(num)-4) :
        num[i] = '*'
    answer = ''.join(num)
    return answer