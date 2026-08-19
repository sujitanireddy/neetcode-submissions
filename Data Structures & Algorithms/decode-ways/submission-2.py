"""
1-26
                        0 1 2 3      
                        1 0 1 2
 
                1             10 
             0               12  1 
                                  2
1 no    
2 no                                                     
n = len(s)

if s[i]: return 0
if i >= n: return 1

BruteForce: 
TC: O(2**n)
SC: (h)
f(i) = f(i+1)
if i <= n-2 and 10  <= int(s[i:i+2]) <= 26:
    f(i) += f(i+2)

Top down memoization: 
cache = {}
TC: O(n)
SC: O(n)
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        cache = {}

        def recurse(i):

            if i >= n:
                return 1

            if s[i] == "0":
                return 0

            if i in cache:
                return cache[i]
            
            #one brach to check if single digit possibility
            cache[i] = recurse(i+1)

            #second branch to check double digit
            if i < n-1 and 10 <= int(s[i:i+2]) <= 26:
                cache[i] += recurse(i+2)

            return cache[i]

        return recurse(0)

"""
0 1 
0 6
n = 2

f(0)

"""