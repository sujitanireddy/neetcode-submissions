class Solution:
    def trap(self, height: List[int]) -> int:

        rain_trapped = 0

        for i in range(len(height)):

            max_left_height = max_right_height = height[i]

            for j in range(i):

                max_left_height = max(max_left_height, height[j])
        
            for j in range(i+1, len(height)):

                max_right_height = max(max_right_height, height[j])
        
            rain_trapped += min(max_right_height, max_left_height) - height[i]
    
        return rain_trapped