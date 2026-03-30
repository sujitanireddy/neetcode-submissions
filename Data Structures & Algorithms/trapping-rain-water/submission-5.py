class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        #Pre-computing the left max heights (Prefix algo)
        left_max_height_so_far = 0
        prefix_left_max_heights = [0] * n
        for i in range(1, n): #skipping the first index as the min will be 0
            left_max_height_so_far = max(left_max_height_so_far, height[i-1])
            prefix_left_max_heights[i] = left_max_height_so_far

        #Pre-computing the right max heights (Postfix algo)
        right_max_height_so_far = 0
        postfix_right_max_heights = [0] * n
        for i in range(n-2, -1, -1): #skipping the last index as the max will be 0
            right_max_height_so_far = max(right_max_height_so_far, height[i+1])
            postfix_right_max_heights[i] = right_max_height_so_far

        
        #formula for calculating the trapped rain water: min(left_max, right_max) - height[i]
        water_trapped_so_far = 0
        for i in range(n):
            water_trapped = min(prefix_left_max_heights[i], postfix_right_max_heights[i]) - height[i]
            if water_trapped < 0:
                continue
            water_trapped_so_far += water_trapped
        
        return water_trapped_so_far

        



        