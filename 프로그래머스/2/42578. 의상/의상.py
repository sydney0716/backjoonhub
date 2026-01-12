def solution(clothes):
    answer = 1
    cloth_counts = {}
    # get count dictionary by .get
    for cloth in clothes:
        cloth_counts[cloth[1]] = cloth_counts.get(cloth[1], 0) + 1
    
    # possible combination is (n0 + 1) * (n1 + 1) ... - 1
    for count in cloth_counts:
        answer *= (cloth_counts[count] + 1)
    
    answer -= 1
    return answer