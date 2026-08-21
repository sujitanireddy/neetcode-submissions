"""
a b c

  0 1 2 3
  a a a a 
    L 
    R

TC: O(n**2)
SC: O(1)

BruteForce:
TC: O(n**3)
SC: O(n)
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0

        #odd check
        for i in range(len(s)):
            L, R = i, i

            while L >= 0 and R < len(s) and s[L] == s[R]:
                L -= 1
                R += 1
                count += 1
        
        #even check
        for i in range(len(s)):
            L, R = i, i+1

            while L >= 0 and R < len(s) and s[L] == s[R]:
                L -= 1
                R += 1
                count += 1
        
        return count