def solution(my_string, queries):
    for s, e in queries :
        substring = list(my_string[s:e+1])
        substring.reverse()
        my_string = my_string[:s] + ''.join(substring) + my_string[e+1:]
    return my_string