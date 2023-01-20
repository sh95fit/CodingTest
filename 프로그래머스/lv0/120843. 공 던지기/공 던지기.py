def solution(numbers, k):
    answer = 0
    count = (k-1)*2
    num = len(numbers)
    if count >= num :
        while(len(numbers)<=count) :
            answer = count - num
            count = count - num
    else :
        answer = count
    return numbers[count]