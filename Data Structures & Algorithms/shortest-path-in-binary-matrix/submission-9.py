class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        length = 1
        
        visited = set()
        visited.add((0,0))
        
        q = deque()
        q.append((0,0))

        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1

        neighbours = [(1,1), (-1,-1),(-1,1),(1,-1),(1,0), (-1,0), (0,1), (0,-1)] #all directions including diags

        while q:

            for _ in range(len(q)):
                r,c = q.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                for dr, dc in neighbours:
                    new_r = r + dr
                    new_c = c + dc
                    
                    if new_r < 0 or new_c < 0 or new_r == ROWS or new_c == COLS or (new_r,new_c) in visited or grid[new_r][new_c] == 1:
                        continue
                    
                    q.append((new_r, new_c))
                    visited.add((new_r, new_c))
                
            length += 1

        return -1 

