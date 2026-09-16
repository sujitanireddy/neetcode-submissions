"""
- min of boundries is the cap of height for water storage
            [0,2,0,3,1,0,1,3,2,1]         
left_bound = 0 0 2 2 3 3 3 3 3 3
right_bound= 3 3 3 3 3 3 2 2 1 0

O(n)
O(n)
"""
class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        left_bounds = [0] * n
        right_bounds = [0] * n

        #calcuate left bounds
        curr_max = 0
        for i in range(1,n):
            curr_max = max(curr_max, height[i-1])
            left_bounds[i] = curr_max
        
        #calculating right bounds
        curr_max = 0
        for i in range(n-2,-1,-1):
            curr_max = max(curr_max, height[i+1])
            right_bounds[i] = curr_max
        
        #computing the water storage at each index
        water_trapped = 0
        res = 0
        for i in range(n):
            water_trapped = (min(right_bounds[i],left_bounds[i])) - height[i]
            if water_trapped > 0:
                res += water_trapped

        return res

        