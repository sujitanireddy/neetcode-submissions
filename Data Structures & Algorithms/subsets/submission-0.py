class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res, temp = [], []
        n = len(nums)

        def build_subsets(i):

            if i == n:
                res.append(temp.copy())
                return

            #don't add
            build_subsets(i+1)

           #add
            temp.append(nums[i])
            build_subsets(i+1)
            temp.pop()
        
        build_subsets(0)
        return res