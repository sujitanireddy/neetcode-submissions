class Solution:
    def trap(self, height: List[int]) -> int:
        
        #area between two bars = min(L and R bar) - h at that spot
        #prefix sums

        #left_bounds = [0,0,2,2,3,3,3,3,3,3,3]
        #right_bounds= [3,3,3,3,3,3,3,3,2,1,0]
        
        n = len(height)
        left_bounds = [0] * n

        height_so_far = 0
        for i in range(1, n):
            height_so_far = max(height_so_far, (height[i-1]))
            left_bounds[i] = height_so_far
        
        right_bounds = [0] * n
        
        height_so_far = 0
        for i in range(n-2, -1, -1):
            height_so_far = max(height_so_far, (height[i+1]))
            right_bounds[i] = height_so_far
        
        water_trapped_so_far = 0
        for i in range(n):
            water_trapped = (min(left_bounds[i], right_bounds[i])) - height[i]
            if water_trapped > 0:
                water_trapped_so_far += water_trapped
        return water_trapped_so_far
                
