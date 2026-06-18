class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = [0] * 26
        L = 0

        max_freq = 0
        
        for R in range(len(s)):

            freq[ord(s[R]) - ord('A')] += 1

            while ((R - L) + 1) - max(freq) > k:

                freq[ord(s[L]) - ord('A')] -= 1

                L += 1
            
            max_freq = max(max_freq, (R - L + 1))
        
        return max_freq

                

