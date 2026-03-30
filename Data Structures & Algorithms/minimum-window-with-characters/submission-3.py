class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""
        
        t_freq_map = defaultdict(int)
        for char in t:
            t_freq_map[char] += 1
        
        s_freq_map = defaultdict(int)
        need = len(t_freq_map)
        have = 0
        L = 0
        best_window = ""

        for R in range(len(s)):

            s_freq_map[s[R]] += 1

            if s[R] in t_freq_map and s_freq_map[s[R]] == t_freq_map[s[R]]:

                have += 1
            
            while need == have:

                window = s[L:R+1]

                if best_window == "" or len(window) < len(best_window):

                    best_window = window
                
                s_freq_map[s[L]] -= 1

                if s[L] in t_freq_map and s_freq_map[s[L]] < t_freq_map[s[L]]:

                    have -= 1

                L += 1
        
        return best_window




        
        
