def solution(n, control):
    dic = {"w": 1, "s": -1, "d": 10, "a": -10}
    answer = n
    for c in control:
        answer += dic[c]
    return answer