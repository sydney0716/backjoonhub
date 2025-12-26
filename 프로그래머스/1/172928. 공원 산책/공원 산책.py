def find_start(mat):
    h = len(mat)
    w = len(mat[0])
    for i in range(h):
        for j in range(w):
            if mat[i][j] == "S":
                return [i, j]

def move(mat, current_coordinate, moving_info):
    h = len(mat)
    w = len(mat[0])
    x = current_coordinate[1]
    y = current_coordinate[0]
    
    direction = moving_info[0]
    moving_length = int(moving_info[1])
       
    y_vector = {"N": -1, "S": 1, "W": 0, "E": 0}
    x_vector = {"N": 0, "S": 0, "W": -1, "E": 1}
    
    destination_x = x + x_vector[direction] * moving_length
    destination_y = y + y_vector[direction] * moving_length
    
    if not (-1 < destination_x < w and -1 < destination_y < h):
        destination_x = x
        destination_y = y
        return current_coordinate
    
    for i in range(1, moving_length + 1):
        if mat[y + y_vector[direction] * i][x + x_vector[direction] * i] == "X":
            return current_coordinate
    return [destination_y, destination_x]
            
def solution(park, routes):
    h = len(park)
    w = len(park[0])
    current_coordinate = find_start(park)
    for route in routes:
        direction_info = route.split()
        current_coordinate = move(park, current_coordinate, direction_info)
            
    return current_coordinate