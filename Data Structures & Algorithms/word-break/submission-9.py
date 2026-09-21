class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)

        dick = {}

        def recurse(i):

            if i in dick:
                return dick[i]

            if i == n:
                return True
            
            for j in range(i, n):

                if s[i:j+1] in wordDict:

                    if recurse(j+1):

                        dick[i] = True

                        return True
            
            dick[i] = False
            return False
        
        return recurse(0)