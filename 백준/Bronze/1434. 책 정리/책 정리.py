def calculate_wasted_space(N, M, box_capacities, book_sizes):
    current_box_index = 0
    current_book_index = 0

    box_fill = [0] * N  

    while current_book_index < M and current_box_index < N:
        if box_fill[current_box_index] + book_sizes[current_book_index] <= box_capacities[current_box_index]:        
            box_fill[current_box_index] += book_sizes[current_book_index]
            current_book_index += 1

        else:           
            current_box_index += 1  
   
    wasted_space = 0

    for i in range(N):
        wasted_space += box_capacities[i] - box_fill[i]

    return wasted_space

N, M = map(int, input().split())
box_capacities = list(map(int, input().split()))
book_sizes = list(map(int, input().split()))

result = calculate_wasted_space(N, M, box_capacities, book_sizes)

print(result)

