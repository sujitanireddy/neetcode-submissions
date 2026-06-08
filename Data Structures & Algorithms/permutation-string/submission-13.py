class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_freq = [0] * 26
        s2_freq = [0] * 26

        m = len(s1)
        n = len(s2)

        if m > n:
            return False
        
        for i in range(m):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            s2_freq[ord(s2[i]) - ord('a')] += 1
        
        if s1_freq == s2_freq:
            return True
        
        for i in range(m,n):
            s2_freq[ord(s2[i]) - ord('a')] += 1
            s2_freq[ord(s2[i-m]) - ord('a')] -= 1
            

            if s1_freq == s2_freq:
                return True
        
        return False