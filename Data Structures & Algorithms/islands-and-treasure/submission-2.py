class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        """
        O(4 ** mn)
        O(m*n)
        3, -1, 0, 1
        2, 2 , 1, -1
        1, -1, 2, -1
        0, -1, 3, 4

        BFS O(m*n)
            O(m*n)
        """
        visit = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        distance = 1
        q = deque()
        neighbors = [(0,1), (1,0), (-1,0), (0,-1)]

        for r in range(ROWS):
            for c in range(COLS):        
                if grid[r][c] == 0:
                    q.append((r,c))
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in neighbors:
                    nr = r + dr
                    nc = c + dc
                
                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == -1 or (nr,nc) in visit or grid[nr][nc] == 0:
                        continue
                    
                    grid[nr][nc] = distance

                    q.append((nr,nc))
                    visit.add((nr,nc))
            
            distance += 1


