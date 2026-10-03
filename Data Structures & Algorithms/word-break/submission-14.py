class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True #if we reach last position then it's true, based on our recursive solution

        for i in range(len(s) - 1, -1, -1):

            for word in wordDict:

                if (i + len(word)) <= len(s) and s[i:i+len(word)] == word:

                    dp[i] = dp[i + len(word)]
                
                if dp[i]:
                    break
        
        return dp[0]