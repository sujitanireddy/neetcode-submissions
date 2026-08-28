"""
0 1 2 3 4      
a b a b d
  L
      R

odd 
even 

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        length = 0

        for i in range(len(s)):

            L , R = i, i

            while L >= 0 and R < len(s) and s[L] == s[R]:
                if ((R-L)+1) > length:
                    length = (R-L)+1
                    res = s[L:R+1]
                L -= 1
                R += 1
        
        for i in range(len(s)):

            L , R = i, i + 1

            while L >= 0 and R < len(s) and s[L] == s[R]:
                if ((R-L)+1) > length:
                    length = (R-L)+1
                    res = s[L:R+1]
                L -= 1
                R += 1
        
        return res
