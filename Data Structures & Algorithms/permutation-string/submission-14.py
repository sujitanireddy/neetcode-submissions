class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
                                 
                                         
        """                        L   R
        s1 = "abc", s2 = "       l e c a b e e            "

        s1_freq_arry = [0] * 26 
        s2_freq_arry = [0] * 26 

        """
        if len(s1) > len(s2):
            return False

        s1_freq_arry = [0] * 26 
        s2_freq_arry = [0] * 26

        for i in range(len(s1)):
            s1_freq_arry[ord(s1[i]) - ord('a')] += 1
            s2_freq_arry[ord(s2[i]) - ord('a')] += 1

        print(s1_freq_arry)
        #print(s2_freq_arry)
        
        if s1_freq_arry == s2_freq_arry:
            return True
        
        L = 0
        for R in range(len(s1), len(s2)):
            s2_freq_arry[ord(s2[L]) - ord('a')] -= 1
            L+=1
            s2_freq_arry[ord(s2[R]) - ord('a')] += 1

            print(s2_freq_arry)

            if s1_freq_arry == s2_freq_arry:
                return True
        
        return False
        
         

