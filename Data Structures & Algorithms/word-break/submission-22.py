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
0   1   2   3   4   5   6   7
n   e   e   t   c   o   d   e
_   _   _   _   T   _   _   _   T

i
j
a   a   a   a   a   a   a
T   F   F   T   T   F   F   T



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

        dp = [False] * len(s)
        dp = dp + [True]

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict_set:
                    dp[i] = dp[i + len(s[i:j+1])]
                
                if dp[i]:
                    break

        return dp[0]

                     











