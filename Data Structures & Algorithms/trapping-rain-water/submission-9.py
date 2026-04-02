class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        left_bounds = [0] * n
        right_bounds = [0] * n

        max_left_bound = 0
        for i in range(1, n):
            max_left_bound = max(max_left_bound, height[i-1])
            left_bounds[i] = max_left_bound
        
        max_right_bound = 0
        for i in range(n-2, -1, -1):
            max_right_bound = max(max_right_bound, height[i+1])
            right_bounds[i] = max_right_bound
        
        water_trapped_so_far = 0
        
        for i in range(n):
            water_trapped = min(left_bounds[i], right_bounds[i]) - height[i]

            if water_trapped > 0:

                water_trapped_so_far += water_trapped
        
        return water_trapped_so_far