class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        """
        len(s) >= len(t): return ""
        need = 3
        have = 2
                        R
              L
        s = O U Z O D Y X A Z V
        s_map = O : 1
                U : 0
                Z : 1
                D : 0
                Y : 0
                X : 1
                A : 1
        t = X Y Z
        t_map = X: 1, Y: 1, Z: 1
        """

        if len(t) > len(s):
            return ""
        
        t_freq = defaultdict(int)
        for c in t:
            t_freq[c] += 1
        
        need = len(t_freq)
        have = 0
        best_window = ""
        L = 0

        s_freq = defaultdict(int)

        for R in range(len(s)):

            s_freq[s[R]] += 1

            if s[R] in t_freq and s_freq[s[R]] == t_freq[s[R]]:
                have += 1

            while need == have:

                window = s[L:R+1]

                if not best_window or len(window) < len(best_window):
                    best_window = window
                
                s_freq[s[L]] -= 1

                if s[L] in t_freq and s_freq[s[L]] < t_freq[s[L]]:
                    have -= 1

                L += 1
        
        return best_window

                







     