"""
Early return:
- if len(s1) + len(s2) != len(s3): return False

Base case:
- If we go out of bounds with both s1, s2 and s3 strings then we can return true 
- if either j or i is out of bounds then don't consider that branch.
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3): 
            return False
        
        cache = {}
        
        def recurse(i,j,k):

            if (i,j,k) in cache:
                return cache[(i,j,k)]
            
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            
            res1, res2, res3 = False, False, False
            
            if i < len(s1) and s1[i] == s3[k]:
                res1 = recurse(i+1,j,k+1)
            
            if j < len(s2) and s2[j] == s3[k]:
                res2 = recurse(i,j+1,k+1)
            
            else:
                res3 = False
            
            cache[(i,j,k)] = res1 or res2 or res3

            return cache[(i,j,k)]
        
        return recurse(0,0,0)