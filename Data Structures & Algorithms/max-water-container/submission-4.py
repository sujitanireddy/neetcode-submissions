class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area = 0

        R = len(heights) - 1
        L = 0 

        while L < R:

            max_area = max(min(heights[L], heights[R]) * (R - L), max_area)

            if heights[L] < heights[R]:
                L += 1
            
            else:
                R -= 1

        return max_area




        