"""
dijstraks algo on matrix

minHeap

"""
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        minHeap = [(grid[0][0],0,0)]
        visit = set()
        neigbours = [(0,1), (1,0), (0,-1), (-1,0)]
        res = 0


        while minHeap:

            elevation,r,c = heapq.heappop(minHeap)
            
            res = max(res, elevation)

            if r == ROWS - 1 and c == COLS - 1:
                return res

            visit.add((r,c))

            for dr, dc in neigbours:
                
                nr = dr + r
                nc = dc + c

                if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr,nc) in visit:
                    continue
                
                heapq.heappush(minHeap, (grid[nr][nc],nr,nc))

        return res