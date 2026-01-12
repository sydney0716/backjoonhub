def solution(nums):
    answer = 0
    pokenmons = set(nums)
    
    if len(nums) // 2 > len(pokenmons):
        answer = len(pokenmons)
    else:
        answer = len(nums) // 2
    
    return answer