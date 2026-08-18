"""
  a b c

  a a a
    L 
      R

O(n**2) = a, a, aaa, a, aa, aa

a, aa, aaa, a, aa, a

Palindrome check = O(n)
TC: O(n**3)
SC: O(1)
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        
        #odd pali check
        for i in range(len(s)):

            L, R = i, i

            while L >= 0 and R < len(s) and s[L] == s[R]:
                res += 1
                L -= 1
                R += 1

        #even pali check
        for i in range(len(s)):

            L, R = i, i+1

            while L >= 0 and R < len(s) and s[L] == s[R]:
                res += 1
                L -= 1
                R += 1
        
        return res