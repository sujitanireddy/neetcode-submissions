class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        """
            [0,1,0]
            [1,0,0]
            [1,1,0]
        edge case: if the first or last index is 1 then return -1
        visit = set() - tracking visited locations
        out of bounds and 1 check
        """
        ROWS = COLS = len(grid)
        
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1
        
        visit = set()
        neighbors = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        distance = 1
        q = deque()
        q.append((0,0))

        while q:

            for _ in range(len(q)):
                r, c = q.popleft()

                if (r,c) == (ROWS-1,COLS-1):
                    return distance

                for dr, dc in neighbors:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 1 or (nr,nc) in visit:
                        continue
                    
                    q.append((nr,nc))
                    visit.add((nr,nc))
            
            distance += 1
        
        return -1 



        
