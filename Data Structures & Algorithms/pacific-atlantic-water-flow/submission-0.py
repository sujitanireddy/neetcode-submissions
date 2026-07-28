class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        """
        Approach: We can do DFS on each cell and see if they reach the pac or atl ocean and save that, but the TC is going to be O(n*m ** 2)
        a better approach is instead of doing DFS on each cell, doing DFS on all the borders and seeing which cells will get water flowing from both atl and pacific is a time effecient approach.

        Implementation:
        - Using a hashset we can store the cells that water can get to from atl and pac
        - Start for borders and do DFS.
        - Water can pass from oceans to the cell only if the previous cell has equal or bigger elevation. As we are thinking about this in a way that we are allowed to place a block of water in that spot.
        - At the end we visit all cells and if any cells are in both sets then we can save that
        """
        res = []
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r,c,visit,prevheight):

            if r < 0 or c < 0 or r == ROWS or c == COLS or ((r,c)) in visit or heights[r][c] < prevheight:
                return
            
            visit.add((r,c))

            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])


        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])

        print(pac)
        print(atl)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res        

