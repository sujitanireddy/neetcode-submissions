"""
0 1
1 2

1 + 1 = 1 
2 = 2

3

1 1 1
1 2
2 1


4
1 1 1 1
2 2 
2 1 1
1 1 2
1 2 1

2 = 2
3 = 3 
4 = 5

0 1 1 2 3 5 8

if n <= 3:
    return n

f(n) = f(n-1) + f(n-2)
2   3   4   
2   3   5
"""
class Solution:
    def climbStairs(self, n: int) -> int:

        if n < 4:
            return n

        dp = [2,3]

        i = 3

        while i < n:

            temp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = temp
            i += 1
        
        return dp[1]









        
