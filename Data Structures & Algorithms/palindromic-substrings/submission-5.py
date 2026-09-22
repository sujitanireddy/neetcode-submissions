"""

                
        L   
        R       
        a   a   a


BruteForce: TC: O(2**n)
Optimal: TC: O(n**2), SC: O(1)
"""
class Solution:
    def countSubstrings(self, s: str) -> int:

        res = 0
        
        #odd palindrome check
        for i in range(len(s)):

            L , R = i, i

            while L >= 0 and R < len(s) and s[L] == s[R]:
                
                res += 1
                
                L -= 1
                R += 1

        #even palindrome check
        for i in range(len(s)):

            L , R = i, i+1

            while L >= 0 and R < len(s) and s[L] == s[R]:
                
                res += 1
                
                L -= 1
                R += 1

        return res

