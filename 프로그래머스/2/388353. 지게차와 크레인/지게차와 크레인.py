from collections import deque

dy_dx = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def check_outside(matrix):
    n, m = len(matrix), len(matrix[0])
    # Make a matrix that shows visited or not
    visited = [[False] * m for _ in range(n)]
    # Start from 0, 0
    queue = deque([(0, 0)])
    visited[0][0] = True
    
    while queue:
        y, x = queue.popleft()
        # Look for 4 direction
        for dy, dx in dy_dx:
            ny, nx = y + dy, x + dx
            
            if -1 < ny < n and - 1 < nx < m:
                # If that container is not visited and empty, append to queue
                if not visited[ny][nx] and matrix[ny][nx] == 0:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
    return visited

def solution(storage, requests):
    answer = 0
    n, m = len(storage), len(storage[0])
    # Make a 0 padded matrix
    mat = [[0] * (m + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(m):
            mat[i + 1][j + 1] = ord(storage[i][j])
    
    # Get request
    for request in requests:
        target = ord(request[0])
        # Check outside container every request
        outside = check_outside(mat)
        # Make a list for removing container
        to_remove = []
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if mat[i][j] == target:
                    if len(request) == 2:
                        # For crane, just remove
                        to_remove.append((i, j))
                    else:
                        # For lift, check outside
                        for dy, dx in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                            if outside[i + dy][j + dx]:
                                to_remove.append((i, j))
                                break
        # Remove container at once at the end
        for r, c in to_remove:
            mat[r][c] = 0

    # Count remaining containers
    for row in mat:
        for container in row:
            if container != 0:
                answer += 1
    return answer