"""
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:

        best_window = 0
        
        for i in range(len(s)):
            L, R = i, i

            while L >= 0 and R < len(s) and s[L] == s[R]:
                if R-L + 1 > best_window:
                    best_window = max(best_window, R-L + 1)
                    substring = s[L:R+1]       
                L -= 1
                R += 1
        
        for i in range(len(s)):
            L, R = i, i+1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if R-L + 1 > best_window:
                    substring = s[L:R+1]
                    best_window = max(best_window, R-L + 1)
                L -= 1
                R += 1

        return substring