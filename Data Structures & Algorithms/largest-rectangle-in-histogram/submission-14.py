class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stk = []
        max_area_so_far = 0

        for i, h in enumerate(heights):

            start = i

            while stk and stk[-1][0] > h:

                stk_h, stk_idx = stk.pop()

                area = stk_h * (i - stk_idx)

                max_area_so_far = max(max_area_so_far, area)

                start = stk_idx                
            
            stk.append((h, start))
        
        l = len(heights)
        
        for h, i in stk:

            max_area_so_far = max(max_area_so_far, (h * (l - i)))

        return max_area_so_far 