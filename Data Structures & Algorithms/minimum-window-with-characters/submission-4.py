class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        #Algorithm
        #Build a hashmap for t string. len(t_map) = need.
        #if need == have then it's valid. Save the window and move L pointer until it's not valid anymore.
        #Keep updating need and have and keep sliding the window and once R is out of bounds. Return the best window found

        t_map = defaultdict(int)
        for char in t:
            t_map[char] += 1
        
        #print(t_map)

        need = len(t_map)
        have = 0
        L = 0
        best_window = ""
        s_map = defaultdict(int)

        for R in range(len(s)):

            s_map[s[R]] += 1

            if s[R] in t_map and s_map[s[R]] == t_map[s[R]]:
                have += 1

            while need == have:

                window = s[L:R+1]

                if not best_window or len(window) < len(best_window):

                    best_window = window
                
                s_map[s[L]] -= 1

                if s[L] in t_map and s_map[s[L]] < t_map[s[L]]:

                    have -= 1
                
                L += 1
            
        return best_window





