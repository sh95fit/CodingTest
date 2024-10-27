def solution(quiz):
    answer = []
    answer = list(map(evaluate, quiz))
    return answer

def evaluate(expression):
    exp, ans = expression.split(" = ")
    exp = eval(exp.strip())
    
    if(exp == int(ans.strip())) :
        return("O")
    else:
        return("X")