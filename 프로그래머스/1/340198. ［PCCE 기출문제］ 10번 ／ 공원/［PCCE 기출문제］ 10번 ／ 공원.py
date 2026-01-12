def check_square(matrix, current_position, n):
    x = current_position[1]
    y = current_position[0]

    if y + n > len(matrix) or x + n > len(matrix[0]):
        return False
    
    for i in range(y, y + n):
        for j in range(x, x + n):
            if matrix[i][j] != "-1":
                return False
    return True        
    
def solution(mats, park):
    mats.sort(reverse=True)
    max_row = len(park)
    max_col = len(park[0])
    
    for size in mats:
        for i in range(max_row - size + 1):
            for j in range(max_col - size + 1):
                if check_square(park, [i, j], size):
                    return size 
                    
    return -1