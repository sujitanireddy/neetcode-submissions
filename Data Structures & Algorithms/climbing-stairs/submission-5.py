"""
f(i) = f(i-1) + f(i-2)

f(4) = f(3) + f(2)
        3 + 2 

if n < 3: return n
"""
class Solution:
    def climbStairs(self, n: int) -> int:

        cache = {}

        def recurse(n):

            if n in cache:
                return cache[n]

            if n < 3:
                 return n     

            cache[n] = recurse(n-1) + recurse(n-2)

            return cache[n]
        
        return recurse(n)