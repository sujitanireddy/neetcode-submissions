"""
0/1 knapsack approach can work I think.
                                                              
                                    0 1 2 3 4 5 6 7 8 9 10 11 12 
                                    a p p l e p e n a p  p  l  e 

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
        
        #Initialization
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):

            for w in wordDict:

                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                
                if dp[i]:
                    break
        
        return dp[0]
