"""
10 / 2 = 5

[1,2,3,4,5]

15 / 2 = 7.5

    i
1,2,3,4

edge case: if sum(nums) % 2 != 0: return False

                          0
i = 0               1            0
i = 1            3     1       2     0
i = 2         6    3 4   1   5   2
 
return True if we find the half of the total sum of nums

Base cases:
- if half_sum == summ: return True
- if summ > half_sum: return False

Recurrence Relation: f(n) = f(summ+nums[i]) or f(nums[i])

BruteForce: TC: O(2**n), SC: O(h)
Top Down Memoization: TC: O(n), SC: O(n)
Bottom up (Dp) : TC: O(n), SC : O(n)
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        half = (sum(nums) // 2)
        
        if sum(nums) % 2 != 0:
            return False

        cache = {}
        
        def recurse(i, summ):

            if (i,summ) in cache:
                return cache[(i,summ)]

            if i == len(nums):
                return False
            
            if half == summ:
                return True
            
            if summ > half:
                return False
            
            cache[(i,summ)] = recurse(i+1, summ + nums[i]) or recurse(i+1, summ)

            return cache[(i,summ)]

        return recurse(0,0)