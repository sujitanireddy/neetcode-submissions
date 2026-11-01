class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        sol = []
        
        def dfs(i):
            
            if i >= len(s):
                res.append(sol[:])
                return
            
            for j in range(i, len(s)):
                word = s[i:j+1]
                if word == word[::-1]:
                    sol.append(word)
                    dfs(j+1)
                    sol.pop()


        dfs(0)

        return res

        