class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)

        cache = {}

        def recurse(i):

            if i in cache:
                return cache[i]

            if i == n:
                return True
            
            for j in range(i, n):

                if s[i:j+1] in wordDict:

                    if recurse(j+1):

                        cache[i] = True

                        return True
            
            cache[i] = False
            return False
        
        return recurse(0)