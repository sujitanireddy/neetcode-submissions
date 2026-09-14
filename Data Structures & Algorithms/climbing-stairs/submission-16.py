"""

3

1,2
1,1,1
2,1


4

1,1,1,1
2,2
1,2
2,1
1,2,1
2,1,1


f(n) = f(n-1) + f(n-2)
f(4) = f(3) + f(2)
"""
class Solution:
    def climbStairs(self, n: int) -> int:

        cache = {}

        def recurse(n):

            if n in cache:
                return cache[n]

            if n < 4:
                return n
        
            cache[n] = recurse(n-1) + recurse(n-2)

            return cache[n]

        return recurse(n)


        
        