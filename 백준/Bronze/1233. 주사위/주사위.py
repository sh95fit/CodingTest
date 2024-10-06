def most_frequent_dice_sum(S1, S2, S3):
    from collections import defaultdict
  
    sum_count = defaultdict(int)
       
    for die1 in range(1, S1 + 1):
        for die2 in range(1, S2 + 1):
            for die3 in range(1, S3 + 1):
                current_sum = die1 + die2 + die3
                sum_count[current_sum] += 1
       
    max_frequency = -1
    most_frequent_sum = None
    
    for sum_value, count in sum_count.items():
        if count > max_frequency:
            max_frequency = count
            most_frequent_sum = sum_value

        elif count == max_frequency:
            most_frequent_sum = min(most_frequent_sum, sum_value)
    
    return most_frequent_sum

S1, S2, S3 = map(int, input().split())

print(most_frequent_dice_sum(S1, S2, S3))

