def solution(s):
    answer = ''
    num_list = s.split()
    max, min = int(num_list[0]), int(num_list[0])
    
    for num in num_list:
        n = int(num)
        if n > max:
            max = n
        if n < min:
            min = n
    
    answer = f"{min} {max}"
    return answer