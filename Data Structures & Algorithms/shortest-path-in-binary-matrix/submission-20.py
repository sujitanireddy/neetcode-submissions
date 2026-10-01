"""
Early return case:
ROWS = len(grid)
COLS = len(grid[0])

- if grid[0][0] or grid[ROWS-1][COLS-1] == 1: return -1

[x,1,x]
[1,x,x]
[1,1,x]

1 + 2

TC: O(m*n)
SC: O(1)
"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        if grid[0][0] or grid[ROWS-1][COLS-1] == 1: 
            return -1
    
        q = deque()
        q.append((0,0))
        grid[0][0] = 1
        neighbours = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        res = 1

        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                if (r,c) == (ROWS-1, COLS-1):
                    return res
                
                for dr, dc in neighbours:
                    nr = dr + r
                    nc = dc + c

                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 1:
                        continue
                    
                    grid[nr][nc] = 1
                    q.append((nr,nc))
            
            res += 1
        
        return -1
                    


