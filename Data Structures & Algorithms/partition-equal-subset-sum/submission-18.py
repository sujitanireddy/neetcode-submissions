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

Bottom up: Tabulation 

To reach target(5) can we do that with the given numbers? 

        0   1   2   3   4   5

1    0  T   T   F   F   F   F

2    1  T   T   T   T   F   F

3    2  T   T   T   T   T   T (Return True)

4    3  F   F   F   F   F   F 


Initalization:
    if c == 0 or c == nums[R]: True

True DP:
    if c > nums[R]:
        matrix[r-1][c - nums[R]]
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 != 0:
            return False
        
        ROWS = len(nums)
        COLS = (sum(nums) // 2) + 1

        matrix = [[False] * COLS for r in range(ROWS)]

        #Initializing first row
        for c in range(COLS):
            if c == 0 or c == nums[0]:
                matrix[0][c] = True
        
        #Dp logic
        for r in range(1,ROWS):
            for c in range(COLS):

                skip = matrix[r-1][c]
                include = False

                if c >= nums[r]:
                    include = matrix[r-1][c - nums[r]]
                
                matrix[r][c] = skip or include
        
        return matrix[ROWS-1][COLS-1]


            
        




















