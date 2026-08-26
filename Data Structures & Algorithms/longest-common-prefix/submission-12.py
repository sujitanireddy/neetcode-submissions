"""
  0 1 2 3
  b a t
  b a g
  b a n 
  b a n


- length of the min word.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_length = float("inf")
        for s in strs:
            min_length = min(len(s), min_length)

        i = 0

        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1
        
        return s[:i]


