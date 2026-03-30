class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #early return 
        if len(s1) > len(s2):
            return False

        #frequency maps of for comparison
        s1_freq_map = defaultdict(int)
        s2_freq_map = defaultdict(int)


        for char in s1:
            s1_freq_map[char] += 1

        
        L = 0
        window_size = len(s1)
        for R in range(len(s2)):
            s2_freq_map[s2[R]] += 1

            if s1_freq_map == s2_freq_map:
                return True
            
            if (R-L)+1 == window_size:
                s2_freq_map[s2[L]] -= 1
            
                if s2_freq_map[s2[L]] == 0:
                    del s2_freq_map[s2[L]]

                
                L += 1
        
        return False





            
            
        
