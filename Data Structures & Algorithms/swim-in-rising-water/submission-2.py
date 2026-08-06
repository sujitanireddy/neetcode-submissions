class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        
        min_heap = [(grid[0][0], 0, 0)]  #elevation, row, col 
        visit = set()
        res = 0

        neighbors = [(0,1),(1,0),(-1,0),(0,-1)] #r,c

        while min_heap:

            e, r, c = heapq.heappop(min_heap)

            res = max(res, e)

            if (r,c) == (ROWS-1, COLS-1):
                return res
            
            for dr, dc in neighbors:

                nr = dr + r
                nc = dc + c

                if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr,nc) in visit:
                    continue
                
                heapq.heappush(min_heap, (grid[nr][nc], nr, nc))

                visit.add((nr,nc))
        
        return res
                





            



