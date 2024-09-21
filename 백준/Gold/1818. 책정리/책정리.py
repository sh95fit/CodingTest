def length_of_lis(sequence):
    from bisect import bisect_left
    
    lis = []

    for value in sequence:
        pos = bisect_left(lis, value)

        if pos == len(lis):
            lis.append(value)

        else:
            lis[pos] = value

    return len(lis)

def min_moves_to_sort_books(N, books):   
    position_map = {book: i for i, book in enumerate(books)}      
    position_sequence = [position_map[i] for i in range(1, N + 1)]       
    lis_length = length_of_lis(position_sequence)
       
    return N - lis_length

N = int(input())
books = list(map(int, input().split()))

print(min_moves_to_sort_books(N, books))

