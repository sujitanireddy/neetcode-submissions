"""

[1,2,3,4]

- if we found a subset which equls half of the sum of the total value then we can instantly return true

total_sum = 10/2 = 5

Base Case:
- if summ == half_sum:
        return True

- if summ > half_sum:
        return False

                                                    [1]               []
                                                
                                            
                                            [1,2]              [1]           [2]                 []

                                    
                                     [1,2,3]     [1,2]    [1,3]   [1]    [2,3]      [2]   [3]           []

Brute Force Recursive way: O(2**n), SC: O(n)
Top down memoizatoin: O(n), SC: O(n)                                        
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2

        cache = {}
        
        def recurse(i,summ):

            if (i,summ) in cache:
                return cache[(i,summ)]
            
            if summ == target:
                return True
            
            if summ > target:
                return False
            
            if i >= len(nums):
                return False
            
            cache[(i,summ)] = recurse(i+1, summ) or recurse(i+1, summ + nums[i])

            return cache[(i,summ)]

        return recurse(0,0)