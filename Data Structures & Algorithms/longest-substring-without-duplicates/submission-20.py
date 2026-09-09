"""
edge case: if not s: return 0

    L
      R
z x y z x y z

{z,x,y  }

      L
      R
x x x x

L
  R
y

{y,z,x}

            L
            R
0 1 2 3 4 5 6
z z z z y x x

{z,y,x}

best_window = 3
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        L = 0
        longest = 0

        for R in range(len(s)):

            while s[R] in seen:

                seen.remove(s[L])

                L += 1
            
            seen.add(s[R])

            longest = max(longest, (R - L) + 1)
        
        return longest

