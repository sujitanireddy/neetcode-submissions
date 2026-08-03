class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        0 1 2 3 4 5 6
          L
                R
        z x y z x y z
        sett = {x,y,z}

        L
          R
        p w w k e w

        """
        if s == " ":
            return 1 

        sett = set()
        length = 0
        L = 0

        for R in range(len(s)):
            
            while s[R] in sett:
                sett.remove(s[L])
                L += 1

            sett.add(s[R])

            length = max(length, (R - L) + 1)
        
        return length