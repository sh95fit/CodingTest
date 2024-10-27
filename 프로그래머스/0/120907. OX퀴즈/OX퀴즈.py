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

# import ast
# import operator

# def solution(quiz):
#     return [evaluate(expression) for expression in quiz]

# def evaluate(expression):
#     exp, ans = expression.split(" = ")
#     calculated_value = evaluate_expression(exp.strip())
    
#     return "O" if calculated_value == int(ans.strip()) else "X"

# def evaluate_expression(expr):
#     node = ast.parse(expr, mode='eval')
#     return eval_node(node.body)

# def eval_node(node):
#     if isinstance(node, ast.BinOp):
#         return OPERATORS[type(node.op)](eval_node(node.left), eval_node(node.right))
#     elif isinstance(node, ast.Num):
#         return node.n
#     else:
#         raise ValueError("Unsupported operation")

# OPERATORS = {
#     ast.Add: operator.add,
#     ast.Sub: operator.sub,
# }