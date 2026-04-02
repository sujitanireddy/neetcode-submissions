class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #algorithm
        #Initate L and R pointers and keep computing the max water
        #Move the pointers inward based on the heights of the bars. The smallest of the two pointer will move


        L = 0
        R = len(heights) - 1 
        max_water_stored = 0

        while L < R:

            area = min(heights[L], heights[R]) * (R - L)

            max_water_stored = max(max_water_stored, area)

            if heights[R] > heights[L]:

                L += 1
            
            else:

                R -= 1
        
        return max_water_stored


