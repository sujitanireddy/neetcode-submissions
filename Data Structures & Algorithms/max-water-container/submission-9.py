class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area_so_far = 0

        L = 0
        R = len(heights) - 1 

        while L < R:

            area = (R - L) * min(heights[L], heights[R])
            max_area_so_far = max(max_area_so_far, area)

            if heights[L] < heights[R]:

                L += 1
            
            else:

                R -= 1
        
        return max_area_so_far
        