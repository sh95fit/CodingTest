def solution(arr, queries):
    for n in queries :
        for i,a in enumerate(arr) :
            if n[0] <= i and n[1] >= i: 
                if i % n[2] == 0 :
                    arr[i] += 1
    return arr