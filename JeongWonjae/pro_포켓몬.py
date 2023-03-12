def solution(nums):
    answer = 0
    set_nums = list(set(nums))
    bi_len_nums = len(nums) // 2
    
    if bi_len_nums >= len(set_nums):
        answer = len(set_nums)  
    else:
        answer = bi_len_nums
    
    return answer