def move_tower(n, current, target):
    moves = []
    tmp = 6 - current - target
    if n == 2:
        moves.append([current, tmp])
        moves.append([current, target])
        moves.append([tmp, target])
    else:
        n -= 1
        print(n)
        moves.extend(move_tower(n, current, tmp))
        moves.append([current, target])
        moves.extend(move_tower(n, tmp, target))

    return moves
 

def solution(n):
    answer = []
    answer = move_tower(n, 1, 3)
    
    return answer