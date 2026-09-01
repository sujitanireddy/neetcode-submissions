"""
edge case: if sum(nums) % 2 != 0: return False

base cases: 
- if i == len(nums): return False
- if sum(nums) // 2 == summ: return Truen
- if sum(nums) // 2 < summ: return False

Memoization: o(n*target) and O(n*target)

Bottom Up: DP

sum([1,2,3,4]) = 10. Target = 5 
 
      summ
    0 1 2 3 4 5
1 0 T T F F F F
2 1 T T T F F F
3 2 F F F F F F
4 3 F F F F F F 

 skip = matrix[r-1][c]
 if c >= nums[r] #when can we include? 
 include = matrix[r-1][c - nums[r]]
 matrix[r][c] = skip or include
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 !=0: return False

        ROWS = len(nums)
        COLS = (sum(nums) // 2) + 1

        matrix = [[False] * COLS for i in range(ROWS)]

        #Initalize the first row
        for c in range(COLS):
            if c == 0 or c == nums[0]:
                matrix[0][c] = True

        #DP Logic
        for r in range(1, ROWS):
            for c in range(COLS):

                skip = matrix[r-1][c]

                include = False

                if c >= nums[r]: #when can we include? 
                    include = matrix[r-1][c - nums[r]]
                
                matrix[r][c] = skip or include
        
        return matrix[ROWS-1][COLS-1]




























        