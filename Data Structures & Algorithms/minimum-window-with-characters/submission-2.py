class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_dict = {}
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
      
        have, need = 0, len(t_dict)
        best_window = ""
        L = 0

        s_dict = {}
        for R in range(len(s)):
            s_dict[s[R]] = s_dict.get(s[R], 0) + 1

            if s[R] in t_dict and s_dict[s[R]] == t_dict[s[R]]:
                have += 1
            
            while have == need:
                
                window = s[L:R+1]

                if not best_window or len(window) < len(best_window):
                    best_window = window
            
                s_dict[s[L]] -= 1
                if s[L] in t_dict and s_dict[s[L]] < t_dict[s[L]]:
                    have -= 1
                
                L += 1
        
        return best_window




        
        