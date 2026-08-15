"""
0,1,2,3,5...

2 = 2
3 = 3


4
1,1,1,1
2,2
1,1,2
2,1,1
1,2,1

f(n) = f(n-1) + f(n-2)

basecase = if <= 3 return n:
            return f(n-1) + f(n-2)

2**n

[3,5]

temp = 3
dp[1] = dp[0] + dp[1]
"""

class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 3:
            return n

        dp = [2,3]
        
        i = 3

        while n > i:
            temp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = temp
            i += 1
    
        return dp[1]



            


        

