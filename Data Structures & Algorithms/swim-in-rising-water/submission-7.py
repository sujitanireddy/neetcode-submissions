"""
dijstra's algo
TC: O(VlogE)
SC: V + E
"""
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        neighbors = [(0,1),(1,0),(0,-1),(-1,0)]

        minHeap = [(grid[0][0],0,0)] #(elev, r, c)
        visit = set()

        while minHeap:

            e, r, c = heapq.heappop(minHeap)

            visit.add((r,c))
            res = max(res, e)

            if (r,c) == (ROWS-1, COLS-1):
                return res

            for dr, dc in neighbors:
                nr = dr + r
                nc = dc + c

                if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr,nc) in visit:
                    continue
                
                visit.add((nr,nc))
                heapq.heappush(minHeap, (grid[nr][nc],nr,nc))

        return res


