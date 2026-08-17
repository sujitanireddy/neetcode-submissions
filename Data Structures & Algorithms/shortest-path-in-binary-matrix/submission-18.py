class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1

        neighbours = [(0,1),(1,0),(0,-1),(-1,0),(-1,1),(1,1),(1,-1),(-1,-1)]
        visit = set()
        q = deque()
        q.append((0,0))
        visit.add((0,0))
        res = 1

        while q:
            for _ in range(len(q)):

                r, c = q.popleft()

                if (r,c) == (ROWS-1, COLS-1): return res

                for dr, dc in neighbours:
                    nr = dr + r
                    nc = dc + c

                    if nr < 0 or nc < 0 or nr == ROWS or nc == ROWS or (nr,nc) in visit or grid[nr][nc] == 1:
                        continue
                    
                    visit.add((nr,nc))
                    q.append((nr,nc))

            res += 1

        return -1

        