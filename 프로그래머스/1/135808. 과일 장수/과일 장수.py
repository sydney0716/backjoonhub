from collections import Counter

def solution(k, m, score):
    answer = 0
    
    counter = Counter(score)
    
    for i in range(k, 0, -1):
        
        while counter[i] >= m:
            answer += i * m
            counter[i] -= m 
        if counter[i] > 0:
            counter[i - 1] += counter[i]
    
    
    return answer