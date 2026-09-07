def binary_transform(x):
    ones = [i for i in x if i == "1"]
    removed_zeros = len(x) - len(ones)
    binary = bin(len(ones))[2:]
    return removed_zeros, binary
    
def solution(s):
    remove_zero_count = 0
    count = 0
    while s != '1':
        count += 1
        x, s = binary_transform(s)
        remove_zero_count += x
        
        if count == 10:
            s = '1'
    answer = [count, remove_zero_count]
    return answer