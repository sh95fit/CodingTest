def solution(i, j, k):
    str_num = ''
    for length in range(i,j+1) :
        str_num += str(length)
    return str_num.count(str(k))