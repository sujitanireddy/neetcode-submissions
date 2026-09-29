"""
    0 1 2
 0 [1,1,0]
 1 [0,1,1]
 2 [0,1,2]

Algorithm:
- find all the rotter fruits in the grid and save them.
- While doing BFS, convert the fresh fruits to rotten fruits
- Travese through the grid and check if any fresh fruits remain, if yes then return -1 else return the time

DS: Queue
Algo: Matrix BFS
TC : O(m*n)
SC : O(m*n)

q = []


"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visit = set()
        time = 0
        neighbours = [(0,-1),(-1,0),(1,0),(0,1)] #4 directions

        #add all rotten fruits to queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))

        #BFS
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                visit.add((r,c))

                for dr, dc in neighbours:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 0 or grid[nr][nc] == 2 or (nr,nc) in visit:
                        continue
                    
                    grid[nr][nc] = 2
                    q.append((nr,nc))
                    
            if q:
                time += 1
        
        #do fresh fruits remain post BFS?
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        
        return time





        