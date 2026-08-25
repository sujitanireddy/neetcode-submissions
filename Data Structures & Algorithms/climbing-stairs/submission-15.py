"""
f(i) = f(i-1) + f(i-2)

f(4) = f(3) + f(2)
        3 + 2 

if n < 3: return n
   
   
[3,5]


"""
class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [2,3]
        i = 3

        if n <= 3:
            return n
        
        while n > i:
            temp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = temp
            i += 1
        
        return dp[1]