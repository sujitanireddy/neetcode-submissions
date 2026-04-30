class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        L = 0
        sett = set()

        for R in range(len(s)):
            
            while s[R] in sett:

                sett.remove(s[L])

                L += 1
            
            sett.add(s[R])

            longest = max(longest, (R - L) + 1)

        return longest 

