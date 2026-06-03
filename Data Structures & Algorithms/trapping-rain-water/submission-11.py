class Solution:
    def trap(self, height: List[int]) -> int:

        length = len(height)

        left_bounds = [0] * length
        right_bounds = [0] * length

        max_left = 0
        for i in range(1, length):
            max_left = max(max_left, height[i-1])
            left_bounds[i] = max_left
        
        max_right = 0
        for i in range((length - 2), -1, -1):
            max_right = max(max_right, height[i+1])
            right_bounds[i] = max_right
        
        max_water_trapped = 0
        for i in range(length):
            water_trapped = min(left_bounds[i], right_bounds[i]) - height[i]
            if water_trapped > 0:
                max_water_trapped += water_trapped
        
        return max_water_trapped
        
