class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        
        prefix_min = [0] * n
        left_max_so_far = 0
        for i in range(1, n):
            left_max_so_far = max(left_max_so_far, height[i-1])
            prefix_min[i] = left_max_so_far
        
        prefix_max = [0] * n
        right_max_so_far = 0
        for i in range(n-2, -1, -1):
            right_max_so_far = max(right_max_so_far, height[i+1])
            prefix_max[i] = right_max_so_far
        
        water_trapped_so_far = 0
        for j in range(n):
            water_trapped = min(prefix_min[j], prefix_max[j]) - height[j]

            if water_trapped < 0:
                water_trapped_so_far += 0
            
            else:
                water_trapped_so_far += water_trapped
        
        return water_trapped_so_far

        



        