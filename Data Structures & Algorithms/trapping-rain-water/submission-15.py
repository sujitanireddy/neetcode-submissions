class Solution:
    def trap(self, height: List[int]) -> int:
        """ 
        
        0,2,0,3,1,0,1,3,2,1

        observations:
        - For water to be trapped we need left and right bounds.
        - The min height of the left and right bounds - the height of bar at that position is that max water that can be soterd at that position.
        - If neg water we don't account

        """

        n = len(height)
        
        left_bounds = [0] * n
        right_bounds = [0] * n
        max_water = 0

        running_bound = 0
        for i in range(1, n):
            running_bound = max(running_bound, height[i-1])
            left_bounds[i] = running_bound
        
        running_bound = 0
        for i in range(n-2, -1, -1):
            running_bound = max(running_bound, height[i+1])
            right_bounds[i] = running_bound
        
        for i in range(n):
            water = min(left_bounds[i], right_bounds[i]) - height[i]
            if water > 0:
                max_water += water
        
        return max_water