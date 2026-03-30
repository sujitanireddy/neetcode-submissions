class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stk = []
        max_area_so_far = 0

        for i, h in enumerate(heights):

            start = i 

            while stk and stk[-1][0] > h:

                popped_h, popped_idx = stk.pop()

                area = popped_h * (i - popped_idx)

                max_area_so_far = max(max_area_so_far, area)

                start = popped_idx
            
            stk.append((h, start))
        

        end_idx = len(heights)
        
        for h, idx in stk:

            max_area_so_far = max(max_area_so_far, h * (end_idx - idx))

        return max_area_so_far