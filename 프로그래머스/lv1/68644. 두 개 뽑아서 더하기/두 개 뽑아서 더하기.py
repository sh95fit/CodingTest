import itertools
def solution(numbers):
    result = []
    for i in itertools.combinations(numbers,2) :
        if sum(i) not in result : 
            result.append(sum(i))
    result.sort()
    return result