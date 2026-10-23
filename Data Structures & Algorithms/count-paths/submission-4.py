"""
Brute Force (memoization):
TC: O(m*n)
SC: O(m*n)

Bottom up approach:

    0     1   2    3   4   5  
0   21   15   10   6   3   1  
1   6     5   4    3   2   1
2   1     1   1    1   1   1

TC: O(m*n)
SC: O(1)

dp      6     5   4    3   2   1
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [1] * n

        for _ in range(m-1):
            new_dp = [1] * n
            for i in range(n-2, -1, -1):
                new_dp[i] = new_dp[i+1] + dp[i]
            dp = new_dp
        
        return dp[0]

