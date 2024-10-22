def solution(nums):
    max_num = len(set(nums))
    max_count = len(nums)//2
    
    return min(max_num, max_count)