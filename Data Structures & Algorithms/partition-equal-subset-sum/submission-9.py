class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        target = sum(nums) // 2

        if sum(nums) % 2 != 0: #We are only given positive integers, so if we want to split into two arrays then we need the total sum to be even.
            return False
        
        ROWS = len(nums)
        COLS = target + 1

        matrix = [[False] * COLS for i in range(ROWS)]

        #Initiating the first row           
        for c in range(COLS):         
            if c == nums[0] or c == 0:
                matrix[0][c] = True

        #Core logic
        for r in range(1, ROWS):
            for c in range(COLS):

                skip = matrix[r-1][c]
                include = False

                if c >= nums[r]:
                    include = matrix[r-1][c - nums[r]]

                matrix[r][c] = skip or include

        return matrix[ROWS-1][COLS-1]

