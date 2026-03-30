class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stk = []
        max_area = 0

        for i, h in enumerate(heights):

            start = i

            while stk and stk[-1][0] > h:

                stk_h, stk_idx = stk.pop()

                current_area = stk_h * (i - stk_idx)

                max_area = max(max_area, current_area)

                start = stk_idx

            stk.append((h, start))
        
        last_index = len(heights)
        
        for h, idx in stk:

            max_area = max(max_area, h * (last_index - idx))
        
        return max_area

            