"""
[1,2,3,4]

early return case: if sum(nums) % 2 != 0 : return False

target = sum(nums) // 2

                            1 2 3 4

                        1                  0
                    
                    3                  1                2               0

                X6       3          4           1           5    2           3    0
            
                    7X      3     8X            4   5

O(2**n)

top down memoization: O(n)
Space : O(n)
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
            
            if i >= len(nums):
                return False
            
            if summ > target:
                return False
            
            if summ == target:
                return True
            
            #include path
            cache[(i,summ)] = recurse(i+1, summ + nums[i]) or recurse(i+1, summ)

            return cache[(i,summ)]

        return recurse(0,0)
        
