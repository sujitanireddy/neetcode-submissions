class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        prev_row = [0] * n

        for i in range(m):

            cur_row = [0] * n
            cur_row[n-1] = 1

            for r in range(n-2, -1, -1):

                cur_row[r] = prev_row[r] + cur_row[r+1]
            
            prev_row = cur_row
        
        return cur_row[0]
