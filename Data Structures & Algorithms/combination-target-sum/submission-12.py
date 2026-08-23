"""
base case: if the sum of arr = target: save and return
 - if sum > target: return
 - TC: O(n C k)
 - SC: O(h) 

                     3 4 5 
                [3]     
            
            [3,3]   [3,4]

        [3,3,3]  [3,3,4]
    
    [3,3,3,3] [3,3,3,4]

[3,3,3,3,3] [3,3,3,3,4]

"""
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        sol = []

        def backtrack(i,summ):

            if i >= len(nums):
                return 

            if summ > target:
                return 
            
            if summ == target:
                res.append(sol[:])
                return
            
            sol.append(nums[i])
            backtrack(i, summ + nums[i])
            sol.pop()

            backtrack(i+1, summ)


        backtrack(0,0)

        return res