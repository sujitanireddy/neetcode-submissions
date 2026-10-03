"""

n   e   e   t   c   o   d   e

neet, code

wordDict = set()


                                    i 
                                       j
c   a   t   s   i   n   c   a   r   s

- if we reach the end of the array: That's a valid sequence. So return True
- keep incrementing j to valided if that word is there?
    - If there then incremnet both i,j
    - else increment only j
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        cache = {}
        wordset = set(wordDict)
        
        def recurse(i):

            if i in cache:
                return cache[i]
            
            if i >= len(s):
                return True

            for j in range(i, len(s)):
                if s[i:j+1] in wordset:
                    if recurse(j+1):
                        cache[i] = True
                        return True
            
            cache[i] = False
            return False

        return recurse(0)