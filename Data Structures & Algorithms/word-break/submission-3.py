"""
0/1 knapsack approach can work I think.
                                                              i
                                    0 1 2 3 4 5 6 7 8 9 10 11 12 13
                                    a p p l e p e n a p  p  l  e s

i = 12                                    

0, 1, 2, 3, 4

s[0:1]
s[0:2]
s[0:3]
s[0:4]
s[0:5]


"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet = set(wordDict)
        n = len(s)
        
        cache = {}

        def recurse(i):

            if i in cache:
                return cache[i]

            if i == n:
                return True

            for j in range(i, n):
                if s[i:j+1] in wordSet:
                    if recurse(j+1):
                        cache[i] = True
                        return True
            
            cache[i] = False
            return False

        return recurse(0)