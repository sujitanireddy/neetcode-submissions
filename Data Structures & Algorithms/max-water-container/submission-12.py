class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_water = 0

        L = 0 
        R = len(heights) - 1

        while L < R:

            breadth = R - L 
            length = min(heights[L], heights[R]) 
            area = length * breadth 
            max_water = max(max_water, area)

            if heights[L] < heights[R]:
                L += 1
            
            else:
                R -= 1
        
        return max_water
