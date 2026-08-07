class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        """
        len(s1) > len(s2): retun False

                         0 1 2 3 4 5 6
        s1 = "abc", s2 = l e c a b e e 
                             L     R

            a b c 
        s1 [1,1,1....]

            a b c 
        s2 [1,0,1....]

        TC: O(n)
        SC: O(1)

        """

        if len(s1) > len(s2): return False

        s1_freq = [0] * 26
        s2_freq = [0] * 26

        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            s2_freq[ord(s2[i]) - ord('a')] += 1
        
        if s1_freq == s2_freq: return True

        L = 0
        for R in range(len(s1), len(s2)):
            s2_freq[ord(s2[R]) - ord('a')] += 1
            s2_freq[ord(s2[L]) - ord('a')] -= 1
            L += 1
            
            if s1_freq == s2_freq: return True

        return False

            