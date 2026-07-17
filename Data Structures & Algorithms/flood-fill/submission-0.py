class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        """
        basescases
        - out of bounds
        - if color is not matching: return  

        Change
        if color is matching change it
        add to visited (so we don't visit it again)

        Backtrack
        remove from visited
        """
        ROWS = len(image)
        COLS = len(image[0])
        visited = set()
        pixel = image[sr][sc]

        def dfs(r,c):

            if r < 0 or c < 0 or r == ROWS or c == COLS or image[r][c] != pixel or (r,c) in visited:
                return
            
            image[r][c] = color
            visited.add((r,c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            visited.remove((r,c))


        dfs(sr,sc)
        return image