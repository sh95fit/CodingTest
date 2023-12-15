def solution(polynomial):
    x_num = 0
    c_num = 0
    polynomial = polynomial.replace(' ','').split('+')
    for i in polynomial :
        if i[-1] == 'x' :
            if len(i) == 1 :
                x_num += 1
            else :
                x_num += int(i[:-1:1])
        else :
            c_num += int(i)
    if c_num != 0 and x_num > 1 :
        return f"{x_num}x + {c_num}"
    elif c_num != 0 and x_num == 1 :
        return f"x + {c_num}"
    elif c_num != 0 and x_num == 0 :
        return f"{c_num}"
    elif c_num == 0 and x_num > 1 :
        return f"{x_num}x"
    elif c_num == 0 and x_num == 1 :
        return f"x"
    else :
        return "0"