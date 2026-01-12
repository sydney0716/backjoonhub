import math

def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    answer = 1
    factors = {}
    for i in range(2, math.ceil(math.sqrt(n)) + 1, 1):
        count = 0
        while (n % i == 0):
            n //= i
            count += 1
        if count != 0:
            factors[i] = count
    if n != 1 and n in factors:
        factors[n] += 1
    else:
        factors[n] = 1
        
    if factors:
        for factor in factors:
            if factor == 1:
                continue
            p = factors[factor]
            answer *=  (factor**(p + 1) - 1) / (factor - 1)
    else:
        answer = n + 1
    
    return answer