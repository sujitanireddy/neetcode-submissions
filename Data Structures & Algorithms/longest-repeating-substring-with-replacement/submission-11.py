class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        L = 0

        longest = 0
        
        freq_map = [0] * 26

        for R in range(len(s)):

            freq_map[ord(s[R]) - ord('A')] += 1

            while ((R - L) + 1) - max(freq_map) > k:

                freq_map[ord(s[L]) - ord('A')] -= 1

                L += 1
            
            longest = max(longest, (R - L) + 1)
        
        return longest
            




            
