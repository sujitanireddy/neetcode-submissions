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

        self.res = 0

        def helper(L,R):

            while L >= 0 and R < len(s) and s[L] == s[R]:
                self.res += 1
                L -= 1
                R += 1

        for i in range(len(s)):
            helper(i,i)
            helper(i,i+1)

        return self.res
            
        
