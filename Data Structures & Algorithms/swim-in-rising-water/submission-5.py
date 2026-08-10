class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        """
        t = elevation
        BFS - shorted distance form 0,0 to (n-1, n-1)
        TC: O(ElogV)
        SC: 
        """
        n = len(grid)
        res = 0
        visit = set()
        minHeap = [(grid[0][0],0,0)] #w,r,c
        neighbors = [(0,1),(1,0),(0,-1),(-1,0)]

        while minHeap:
            w, r, c = heapq.heappop(minHeap)
            
            visit.add((r,c))
            res = max(res, w)

            if (r,c) == (n-1,n-1):
                return res

            for dr, dc in neighbors:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nc < 0 or nr == n or nc == n or (nr,nc) in visit:
                    continue
                
                heapq.heappush(minHeap, (grid[nr][nc], nr, nc))
                    

                
