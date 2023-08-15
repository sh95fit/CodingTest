def solution(n_str):
    n_str = list(n_str)
    r_str = list(n_str)
    for n in n_str:
        if n == "0" :
            del r_str[0]
        else :
            return(''.join(r_str))