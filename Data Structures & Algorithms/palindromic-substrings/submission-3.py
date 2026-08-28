"""
i
a b c

  L. 
    R
a a a

O(n**2)
O(1)

odd check
L = 0 R = 0
if s[L] == s[R]

even check
L = 0, R = 1

"""
class Solution:
    def countSubstrings(self, s: str) -> int:

        res = 0
        
        for i in range(len(s)):

            L, R = i, i

            while L >= 0 and R < len(s) and s[L] == s[R]:
                res += 1
                L -= 1
                R += 1

        for i in range(len(s)):

            L, R = i, i + 1

            while L >= 0 and R < len(s) and s[L] == s[R]:
                res += 1
                L -= 1
                R += 1
        
        return res
        
            
        
