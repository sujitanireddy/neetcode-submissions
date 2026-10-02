"""
Notes:
- Currheight > Prevheight

[4,2,7,3,4]
[7,4,6,4,7]
[6,3,5,3,6]


Algo:
- DFS of pacific adj cordinates and add them to a pac set
- DFS on atlantic adj cordinates and add visited cordinates to atl set
- go through all cordinates and see if they are in both atl and pac sets, if they are add them to res
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(heights)
        COLS = len(heights[0])
        atl = set()
        pac = set()
        res = []

        def dfs(r,c,visit,prevHeight):
            
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or heights[r][c] < prevHeight:
                return
            
            visit.add((r,c))

            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])


        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS - 1, atl, heights[r][COLS - 1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        return res