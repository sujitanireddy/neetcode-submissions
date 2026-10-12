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
TC: O(n**2 * m)
SC: O(n)


                i
                            j 
0   1   2   3   4   5   6   7   
n   e   e   t   c   o   d   e 

_   _   _   _   _   _   _   _   T

"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):

                if s[i:j+1] in wordSet:
                    dp[i] = dp[i + len(s[i:j+1])]
                    
                    if dp[i]:
                        break
        
        return dp[0]














