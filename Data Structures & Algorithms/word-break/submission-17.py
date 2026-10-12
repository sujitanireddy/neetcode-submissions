"""
- convert the wordDict to a hashset

                                i
                                j
n   e   e   t   c   o   d   e

            i
            j

c   a   t   s   i   n   c   a   r   s

i
                j
c   a   r   s

{bar}

Keep track of (i,j)

Base case:
- If i goes out of bounds, then we can return True

Conditions:
- If the word in hashset: recurse(i+1,j+1)
- else: recurse(i, j+1)

Brute Force:
TC: O(2**(n*m))
SC: O(n*m)

Top Down Memoization:
TC: O(n**2)
SC: O(n**2)

                i
            j
n   e   e   t   c   o   d   e

"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordSet = set(wordDict)
        cache = {}
        
        def recurse(i):

            if i in cache:
                return cache[i]
            
            if i >= len(s):
                return True

            for j in range(i, len(s)):
                if s[i:j+1] in wordSet:
                    if recurse(j+1):
                        cache[i] = True
                        return cache[i]          
            
            cache[i] = False
            return False

        return recurse(0)