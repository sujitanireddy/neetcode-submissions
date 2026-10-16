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
"""
class Solution:
    def climbStairs(self, n: int) -> int:

        cache = {}
        
        def dfs(i):

            if i in cache:
                return cache[i]
            
            if i <= 3:
                return i
        
            cache[i] = dfs(i-1) + dfs(i-2)
            return cache[i]

        return dfs(n)


