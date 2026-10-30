class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        length = len(height)
        left_bounds = [0] * length
        right_bounds = [0] * length
        
        for i in range(1, length):
            left_bounds[i] = max(height[i-1], left_bounds[i-1])
        
        for i in range(length - 2, -1, -1):
            right_bounds[i] = max(height[i+1], right_bounds[i+1])
            
        for i in range(length):
            water = min(left_bounds[i], right_bounds[i]) - height[i]
            if water > 0:
                total_water += water
        
        return total_water