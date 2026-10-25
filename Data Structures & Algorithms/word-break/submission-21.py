"""

                                i
                                j
n   e   e   t   c   o   d   e

                                    i
                                        j
c   a   t   s   i   n   c   a   r   s

                                                    i
                                                    j
a   p   p   l   e   p   e   n   a   p   p   l   e


            i
                        j
a   a   a   a   a   a   a


wordDict=["aaaa","aaa"]


Notes:
- Convert the wordDict array into a set.

- if j >= len(s):
    return False

- if i >= len(s) and j >= len(s):
    return True

- if s[i:j+1] not in wordDict:
    dfs(i, j+1)
  
  else:
    dfs(j+1,j+1)

"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordDict_set = set(wordDict)

        cache = {}
        
        def dfs(i,j):

            if (i,j) in cache:
                return cache[(i,j)]
            
            if i >= len(s) and j >= len(s):
                return True
            
            if j >= len(s):
                return False
            
            skip = choose = False
            
            if s[i:j+1] in wordDict_set:
                choose = dfs(j+1, j+1)
            
            skip = dfs(i, j+1)

            cache[(i,j)] = skip or choose

            return cache[(i,j)]

        return dfs(0,0)