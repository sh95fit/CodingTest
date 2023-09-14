def solution(ineq, eq, n, m):
    if eq != "!" :
        return int(eval(f"{n} {ineq}{eq} {m}"))
    else :
        return int(eval(f"{n} {ineq} {m}"))