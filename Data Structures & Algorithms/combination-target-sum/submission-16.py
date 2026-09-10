"""
input parameters: nums (no duplicates), target
                                 i 
                              [2,5,6,9]      9

                            [2]         []

                        [2,2]   [2,5]
                    
                    [2,2,2]  [2,2,5]

                [2,2,2,2]  [2,2,2,5]
            
            [2,2,2,2,2]  [2,2,2,2,5]

Base Case:

- if i >= len(nums):
    return

- if summ == target:
    res.append(sol.copy())
    return

- if summ > target:
    return

TC: N C K
SC: O(h)

"""
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        sol = []

        def backtrack(i, summ):
            
            if i >= len(nums):
                return
            
            if summ == target:
                res.append(sol.copy())
                return
            
            if summ > target:
                return
            
            #Choose the number
            sol.append(nums[i])
            backtrack(i, summ + nums[i])
            sol.pop()
        
            #don't choose
            backtrack(i+1, summ)

        backtrack(0,0)

        return res

                    
                    
