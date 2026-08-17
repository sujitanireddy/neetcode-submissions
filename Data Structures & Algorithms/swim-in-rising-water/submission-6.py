"""
Notes:
- time(t) == water level (t)
- vertical, horizontal 
- org elev <= water level (t)

start = 0,0
end = bottom right corner

Dijstra's
"""
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        ROWS = len(grid) 
        COLS = len(grid[0])
        
        minHeap = [(grid[0][0],0,0)] #elevation, r,c
        visit = set()
        res = 0
        neighbours = [(0,1),(1,0),(0,-1),(-1,0)]

        while minHeap:

            elevation, r, c = heapq.heappop(minHeap)

            res = max(res, elevation)

            if (r,c) == (ROWS-1, COLS-1):
                return res
            
            for dr, dc in neighbours:
                nr = dr + r
                nc = dc + c

                if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr,nc) in visit:
                    continue
                
                heapq.heappush(minHeap, (grid[nr][nc], nr, nc))
                visit.add((nr,nc))
        
        return res