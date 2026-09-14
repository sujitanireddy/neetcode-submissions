"""
3

1,2
1,1,1
2,1



1,2,  3,5,8
2,3


f(n) = f(n-1) + f(n-2)
f(4) = f(3) + f(2)
"""
class Solution:
    def climbStairs(self, n: int) -> int:

        if n < 4:
            return n

        dp = [1,2]

        for i in range(2, n):
            temp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = temp
        
        return dp[1]


    
"""
[2,3]

temp = 2

2,3
"""

        
        