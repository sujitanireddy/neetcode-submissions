class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        sett = set()
        L = 0
        longest_substring_seen = 0

        for R in range(len(s)):

            while s[R] in sett:
                sett.remove(s[L])
                L += 1
            
            else:
                longest_substring_seen = max(longest_substring_seen, (R - L) + 1)
            
            sett.add(s[R])
        
        return longest_substring_seen
        