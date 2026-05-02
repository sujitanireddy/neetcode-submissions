class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #area of rectagle = l * b 
        #l = height of the bar
        #b = (R - L)

        #given two bars the (min of the heights) = l
        #  L           R
        #i0,1,2,3,4,5,6,7
        #[1,7,2,5,4,7,3,6]

        max_area = 0
        L = 0
        R = len(heights) - 1

        while L < R:

            area = min(heights[L], heights[R]) * (R - L)
            
            max_area = max(max_area, area)

            if heights[L] <= heights[R]:
                L += 1

            else:
                R -= 1
        
        return max_area