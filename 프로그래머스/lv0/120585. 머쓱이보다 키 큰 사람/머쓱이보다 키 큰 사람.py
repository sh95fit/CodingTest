def solution(array, height):
    answer = 0
    for i in sorted(array, reverse=False) :
        if i > height :
            answer += 1
    return answer