import numpy as np

def solution(wallpaper):
    answer = []
    row_len = len(wallpaper)
    col_len = len(wallpaper[0])
    
    min_row = row_len
    min_col = col_len
    max_row, max_col = 0, 0
    
    for row in range(row_len):
        for col in range(col_len):
            if wallpaper[row][col] == "#":
                if min_row > row:
                    min_row = row
                    
                if min_col > col:
                    min_col = col
                    
                if max_row < row:
                    max_row = row
                    
                if max_col < col:
                    max_col = col
                    
                    
    answer = [min_row, min_col, max_row + 1, max_col + 1]  
    
    
    return answer