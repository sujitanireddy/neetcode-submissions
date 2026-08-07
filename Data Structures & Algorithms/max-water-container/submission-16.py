class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        """
                  LR 

        0 1 2 3 4 5 6 7
        1 7 2 5 4 7 3 6

        while L < R

        """

        L = 0 
        R = len(heights) - 1
        max_water = 0

        while L < R:

            water = (min(heights[L], heights[R])) * (R - L)
            max_water = max(max_water, water)

            if heights[L] <= heights[R]:
                L += 1
            
            else:
                R -= 1
        
        return max_water

        