def solution(n, w, num):
    def get_column(k, width):
        floor = (k - 1) // width
        remainder = (k - 1) % width
        if floor % 2 == 0:
            return remainder
        else:
            return width - 1 - remainder

    target_col = get_column(num, w)
    end_col = get_column(n, w)
    
    top_floor = (n - 1) // w
    target_floor = (num - 1) // w
    
    answer = top_floor - target_floor
    
    last_floor_is_even = top_floor % 2 == 0
    
    if last_floor_is_even:
        if target_col <= end_col:
            answer += 1
    else:
        if target_col >= end_col:
            answer += 1
            
    return answer