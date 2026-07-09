class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        """
                                      aab
                            
                            [a]       [aa]       [aab]X
                        
                        [a]           [b]
                    
                    [b]

        Base case
        - Out of bounds: return
        - If palindrome then save it and backtrack
        """

        res = []
        sol = []


        def backtrack(i):

            #basecase
            if i == len(s):
                res.append(sol[:])
                return

            for j in range(i, len(s)):
                string = s[i:j+1]
                print(string)
                if string == string[::-1]:
                    sol.append(string)
                    backtrack(j+1)
                    sol.pop()


        backtrack(0)
        return res