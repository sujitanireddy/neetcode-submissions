class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        #Algorithm
        #Build a freq map called t_freq_map. Ex: {X:1, Y:1, Z:1}
        #The len of t_freq_map is what we "need" to call it a valid substring
        #Keep building the s_freq_map.
            #If a char is in t_freq_map and the freqencies match then update have += 1
            #if need == have 
                #Slice the window and if your window in the shortest we have seen then save in best_window
                #Move left pointer and while moving validate if the char is in t_freq_map and the freq is less than 
                #required and if it is then have -= 1
        #return the best_window seen by far

        t_freq_map = defaultdict(int)
        for char in t:
            t_freq_map[char] += 1
        
        need = len(t_freq_map)
        have = 0
        best_window = ""
        L = 0
        s_freq_map = defaultdict(int)

        for R in range(len(s)):
            s_freq_map[s[R]] += 1

            if s[R] in t_freq_map and s_freq_map[s[R]] == t_freq_map[s[R]]:
                have += 1
            
            while need == have:

                current_window = s[L:R+1]

                if not best_window or len(current_window) < len(best_window):
                    best_window = current_window
                
                s_freq_map[s[L]] -= 1

                if s[L] in t_freq_map and s_freq_map[s[L]] < t_freq_map[s[L]]:
                    have -= 1
                
                L += 1
        
        return best_window
