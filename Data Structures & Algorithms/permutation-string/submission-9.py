class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        m = len(s1)
        n = len(s2)

        if m > n:
            return False 
    
        s1_freq = [0] * 26
        s2_freq = [0] * 26
        for i in range(m):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            s2_freq[ord(s2[i]) - ord('a')] += 1
        
        if s1_freq == s2_freq:
            return True
        
        L = 0
        for R in range(m, n):
            s2_freq[ord(s2[R]) - ord('a')] += 1
            s2_freq[ord(s2[R - m]) - ord('a')] -= 1

            if s1_freq == s2_freq:
                return True
        
        return False