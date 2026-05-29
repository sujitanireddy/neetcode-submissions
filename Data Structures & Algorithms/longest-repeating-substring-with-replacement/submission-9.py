class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        #sliding window algorithm

        longest = 0

        L = 0

        freq = [0] * 26
        
        for R in range(len(s)):

            freq[ord(s[R]) - ord('A')] += 1

            if ((R - L) + 1) - max(freq) > k:

                freq[ord(s[L]) - ord('A')] -= 1

                L += 1
            
            longest = max(longest, ((R - L) + 1))
        
        return longest

                






