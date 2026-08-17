class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        
        #add all rotten fruits to queue
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
        
        print(q)
        #BFS
        time = 0
        visit = set()
        neighbours = [(0,1),(1,0),(0,-1),(-1,0)]
       
        while q:
            for _ in range(len(q)):
                
                r,c = q.popleft()

                for dr, dc in neighbours:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr,nc) in visit or grid[nr][nc] == 2 or grid[nr][nc] == 0:
                        continue

                    grid[nr][nc] = 2
                    visit.add((nr,nc))
                    q.append((nr,nc))
            
            #print(grid)
            
            if q:
                time += 1

        #check if any rotten fruit remaim

        print(grid)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        
        return time






