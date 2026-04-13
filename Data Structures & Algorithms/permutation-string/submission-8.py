class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        s1_freq = [0] * 26

        for char in s1:
            s1_freq[ord(char) - ord('a')] += 1

        L = 0
        
        window = len(s1)
        s2_freq = [0] * 26

        for R in range(len(s2)):

            s2_freq[ord(s2[R]) - ord('a')] += 1

            if s1_freq == s2_freq:
                    return True

            if (R - L + 1) == window:

                s2_freq[ord(s2[L]) - ord('a')] -= 1
                L += 1
        
        return False

                 


