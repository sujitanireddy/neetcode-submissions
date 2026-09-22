"""

    0 1 2 3 4      
      L 
      R   
    a b a b d

3 - 1= 2 + 1 = 3
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        curr_window = 0
        res = ""
        
        for i in range(len(s)):

            L, R = i, i

            while L >= 0 and R < len(s) and s[L] == s[R]:

                if R - L + 1 > curr_window:
                    curr_window = R - L + 1
                    res = s[L:R+1]
                
                L -= 1
                R += 1
        
        for i in range(len(s)):
            L, R = i, i + 1

            while L >= 0 and R < len(s) and s[L] == s[R]:
                
                if R - L + 1 > curr_window:
                    curr_window = R - L + 1
                    res = s[L:R+1]
                
                L -= 1
                R += 1


        return res