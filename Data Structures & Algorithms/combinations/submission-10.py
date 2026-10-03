"""
n = 3, k = 2

                                    

                                [1]          []
                            
                            [1,2]   [1]     [2]     []

                                [1,3]  [1]  [2,3]   [2]

"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        sol = []
        res = []

        def backtrack(i):
            
            if len(sol) == k:
                res.append(sol.copy())
                return
            
            if i > n:
                return

            #skip
            backtrack(i+1)

            #include
            sol.append(i)
            backtrack(i+1)
            sol.pop()


        backtrack(1)
        
        return res