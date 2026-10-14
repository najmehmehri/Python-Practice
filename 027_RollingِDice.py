import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    board = input_data[2:2 + n]
    
    start_r = -1
    start_c = -1
    for r in range(n):
        for c in range(m):
            if board[r][c] == 's':
                start_r = r
                start_c = c
                break
        if start_r != -1:
            break

    start_state = (start_r, start_c, 6, 4, 2)
    
    queue = deque([start_state])
    
    visited = set()
    visited.add(start_state)
    
    scored_cells = set()
    
   
    moves = [
        (-1, 0, lambda top, north, west: (7 - north, top, west)),
        (1, 0, lambda top, north, west: (north, 7 - top, west)),
        (0, 1, lambda top, north, west: (west, north, 7 - top)),
        (0, -1, lambda top, north, west: (7 - west, north, top))
    ]
    
    while queue:
        r, c, top, north, west = queue.popleft()
        
        cell_val = board[r][c]
        if cell_val.isdigit() and int(cell_val) == top:
            scored_cells.add((r, c))
        
        for dr, dc, roll_dice in moves:
            nr = r + dr
            nc = c + dc
            
            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] != 'x':
                ntop, nnorth, nwest = roll_dice(top, north, west)
                next_state = (nr, nc, ntop, nnorth, nwest)
                
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append(next_state)

    print(len(scored_cells))

if __name__ == '__main__':
    solve()
