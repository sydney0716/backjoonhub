def solution(friends, gifts):
    answer = 0
    n = len(friends)
    gift_matrix = [[0 for _ in range(n)] for _ in range(n)]
    gift_index = [[0, 0, 0] for _ in range(n)]
    next_month_gift = [0] * n
    
    for gift in gifts:
        sender, receiver = gift.split()
        sender_index = friends.index(sender)
        receiver_index = friends.index(receiver) 
        gift_matrix[sender_index][receiver_index] += 1
        
        gift_index[sender_index][0] += 1
        gift_index[receiver_index][1] += 1
        
    for row in gift_index:
        row[2] = row[0] - row[1]
        
    for i in range(n):
        for l in range(i + 1, n):
            if gift_matrix[i][l] > gift_matrix[l][i]:
                next_month_gift[i] += 1
            elif gift_matrix[i][l] < gift_matrix[l][i]:
                next_month_gift[l] += 1
            else:
                if gift_index[i][2] > gift_index[l][2]:
                    next_month_gift[i] += 1
                elif gift_index[l][2] > gift_index[i][2]:
                    next_month_gift[l] += 1

    for element in next_month_gift:
        answer = max(element, answer)
    return answer