"""
n = 3
n = 2
n = 1

f(4) = f(2) + f (3)
f(5) = f(3) + f(4)


1,1,1,1
1,1,2
2,1,1
1,2,1
2,2

Brute force Recursion:
Base case: if n <= 3: return n
f(n) = f(n-2) + f(n-1)
TC: O(2**n)
SC: O(h)

Top Down: Memoization
cache: hashmap
TC: O(n)
SC: O(n)

Bottom up:

f(5)


counter = 1
dp = [1,2]
     [2,3]
     [3,5]
     [5,8]

while counter < n:
    temp = dp[1]
    dp[1] = dp[0] + temp
    dp[0] = temp

"""

class Solution:
    def climbStairs(self, n: int) -> int:

        counter = 1
        dp = [1,2]

        while counter < n:
            temp = dp[1]
            dp[1] = dp[0] + temp
            dp[0] = temp
            counter += 1

        return dp[0] 


        