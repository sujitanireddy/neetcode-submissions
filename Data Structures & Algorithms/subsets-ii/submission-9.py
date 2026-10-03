"""

                                    [1,2,1]
                                
                            [1]                 []

                        [1,2]    [1]         [2]     []

                    [1,2,1]   [1,2]     [1,1]   [1]    [2,1]    [2]     [1]     [] 


- if we skip a no. We should never pick that number again in our recuirsive path
     
     i
 0 1 2
[1,1,2]

TC: n * (2**n)
SC: O(2**n)
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        
        sol = []
        res = []

        def backtrack(i):
            
            if i >= len(nums):
                res.append(sol.copy())
                return

            #including
            sol.append((nums[i]))
            backtrack(i+1)
            sol.pop()
            
            #skip
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)

        backtrack(0)
        return res










