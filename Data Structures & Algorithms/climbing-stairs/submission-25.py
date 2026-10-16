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

        dp = [0] * (n - 1)
        dp[0] = 2
        dp[1] = 3

        for i in range(2, n-1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n-2]
