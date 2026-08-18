"""

"""



class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""

        #odd check
        for i in range(len(s)):
            
            L, R = i, i

            while L >= 0 and R < len(s) and s[L] == s[R]:
                if len(s[L:R+1]) > len(res):
                    res = s[L:R+1]
                L -= 1
                R += 1

        
        #even check
        for i in range(len(s)):
            
            L, R = i, i+1

            while L >= 0 and R < len(s) and s[L] == s[R]:
                if len(s[L:R+1]) > len(res):
                    res = s[L:R+1]
                L -= 1
                R += 1
        
        return res