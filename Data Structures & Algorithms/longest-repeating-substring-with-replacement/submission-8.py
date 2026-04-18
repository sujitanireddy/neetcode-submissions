class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        L = 0
        s_freq = [0] * 26 
        longest = 0
        
        for R in range(len(s)):

            s_freq[ord(s[R]) - ord('A')] += 1

            while ((R - L) + 1) - max(s_freq) > k:

                s_freq[ord(s[L]) - ord('A')] -= 1

                L += 1
            
            longest = max(longest, (R - L + 1))

        return longest





