class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stk = []
        max_area_so_far = 0

        for i, h in enumerate(heights):

            index = i

            while stk and stk[-1][0] > h:

                stk_h, stk_i = stk.pop()

                area = stk_h * (i - stk_i)

                max_area_so_far = max(max_area_so_far, area)

                index = stk_i
            
            stk.append((h, index))
        
        
        length = len(heights)

        for h, i in stk:
            max_area_so_far = max(max_area_so_far, (h * (length - i)))

        return max_area_so_far