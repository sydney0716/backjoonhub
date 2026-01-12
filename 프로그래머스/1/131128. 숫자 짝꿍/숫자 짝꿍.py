from collections import Counter

def solution(X, Y):
    x_counter = Counter(X)
    y_counter = Counter(Y)
    answer = []
    no_match = True
    
    for i in range(9, -1, -1):
        i_str = str(i)
        x_count = x_counter.get(i_str, 0)
        y_count = y_counter.get(i_str, 0)
        friend_count = min(x_count, y_count)
        
        if friend_count != 0:
            no_match = False
            answer.append(i_str*friend_count)

                
    if no_match:
        answer = "-1"
    else:
        answer = "".join(answer)
    
    if answer[0] == '0':
        answer = "0"
        
        
        
    return answer
