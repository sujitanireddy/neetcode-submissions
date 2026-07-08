class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        """ 
        n = 3, k = 2

        1, 2, 3

                             []
                    
                    [1]      [2]      [3]

                [1,2] [1,3] [2,3]

        [[1,2], [1,3], 

        """

        res = []
        sol = []

        def backtrack(i):

            #basecase
            if len(sol) == k:
                res.append(sol[:])
                return
            
            for j in range(i, n+1):
                sol.append(j)
                backtrack(j+1)
                sol.pop()
            
        backtrack(1)
        return res