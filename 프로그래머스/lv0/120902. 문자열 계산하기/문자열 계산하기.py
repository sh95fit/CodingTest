def solution(my_string):
    my_string = my_string.split()
    answer = int(my_string[0])
    for i in range(1,len(my_string)) :
        if my_string[i] == '+' :
            answer += int(my_string[i+1])
        elif my_string[i] == '-' :
            answer -= int(my_string[i+1])
    return answer
#     for i in range(len(my_string)) :
#         if my_string[i] == '-' :
#             sub.append(my_string[i+1])
            
#     for i in sub :
#         while i in my_string :
#             my_string.remove(i)
            
#     while '+' in my_string :
#         my_string.remove('+')
#     while '-' in my_string :
#         my_string.remove('-')

#     my_string = list(map(int,my_string))
#     sub = list(map(int,sub))
#     return sum(my_string) - sum(sub)