class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        length = len(nums)
        sol, res = [], []
        i=0

        def backtrack():

            if length == len(sol):
                res.append(sol.copy())
                return
            
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()

        backtrack()
        return res