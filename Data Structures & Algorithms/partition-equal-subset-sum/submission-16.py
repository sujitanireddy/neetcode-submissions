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


       0 1 2 3 4 5
   1 0 T T F F F F
   2 1 T T T T F F
   3 2 T T T T T T
   4 3 T T T T T T

With the first num in nums. Can we form that value given the c.

"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 != 0:
            return False

        ROWS = len(nums)
        COLS = (sum(nums) // 2) + 1

        matrix = [[False] * COLS for i in range(ROWS)]

        #First row initialization
        for c in range(COLS):
            if c == 0 or c == nums[0]:
                matrix[0][c] = True
        
        #Core logic
        for r in range(1, ROWS):
            for c in range(COLS):

                skip = matrix[r-1][c]

                include = False

                if nums[r] >= matrix[r][c]:
                    include = matrix[r-1][c-nums[r]]
                
                matrix[r][c] = skip or include
        
        return matrix[ROWS-1][COLS-1]







        