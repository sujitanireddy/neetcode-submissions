"""
                i  
n e e t c o d e
wordDict = set()

BruteForce : O(2**n)

"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        cache = {}
        wordSet = set(wordDict)
        n = len(s)

        def recurse(i):

            if i in cache:
                return cache[i]
            
            if i == n:
                return True
            
            for j in range(i,n):
                if s[i:j+1] in wordSet:
                    if recurse(j+1):
                        cache[i] = True
                        return True
            
            cache[i] = False
            return False

        return recurse(0)