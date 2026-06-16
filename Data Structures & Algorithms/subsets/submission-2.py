class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        temp = []
        res = []

        def backtrack(i):

            if n == i:
                res.append(temp.copy())
                return
            
            #don't choose
            backtrack(i+1)

            temp.append(nums[i])
            backtrack(i+1)
            temp.pop()

        backtrack(0)

        return res
