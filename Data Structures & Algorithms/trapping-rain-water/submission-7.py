class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        prefix_array = [0] * n
        postfix_array = [0] * n
        water_trapped_so_far = 0

        max_height_so_far = 0
        for i in range(1, n):
            max_height_so_far = max(max_height_so_far, height[i-1])
            prefix_array[i] = max_height_so_far
        
        max_height_so_far_right = 0
        for i in range(n-2, -1, -1):
            max_height_so_far_right = max(max_height_so_far_right, height[i + 1])
            postfix_array[i] = max_height_so_far_right
        
        for i in range(n):

            water_trapped = min(prefix_array[i], postfix_array[i]) - height[i]

            if water_trapped > 0:

                water_trapped_so_far += water_trapped
        
        return water_trapped_so_far

         