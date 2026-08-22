"""

    1 0 1 2
base case:
if s[i] == 0: return 0
if s[i] >= len(s): return 1

10 <= s[i:i+2] <= 26
check 1: single digit : 0
check 2: double digit : 1

if we are able to decode the entire string: counter += 1

"""
class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        cache = {}

        def recurse(i):

            if i >= n:
                return 1

            if i in cache:
                return cache[i]

            if s[i] == "0":
                return 0
            
            cache[i] = recurse(i+1)

            if i < n-1 and 10 <= int(s[i:i+2]) <= 26:
                cache[i] += recurse(i+2)
            
            return cache[i]
        
        return recurse(0)
            