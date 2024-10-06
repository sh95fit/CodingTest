def find_most_sold_book():
    import sys
    from collections import defaultdict

    input = sys.stdin.read
    data = input().splitlines()    
    N = int(data[0])  
    book_count = defaultdict(int)
        
    for i in range(1, N + 1):
        title = data[i]
        book_count[title] += 1
       
    most_sold = ""
    max_count = 0
     
    for title, count in book_count.items():
        if count > max_count or (count == max_count and title < most_sold):
            most_sold = title
            max_count = count
            
    print(most_sold)

find_most_sold_book()

