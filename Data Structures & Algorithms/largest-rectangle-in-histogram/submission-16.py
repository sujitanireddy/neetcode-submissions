class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stk = []
        largest_rect = 0

        for i, h in enumerate(heights):

            start = i

            while stk and stk[-1][0] > h:

                stk_h, stk_idx = stk.pop()

                largest_rect = max(largest_rect, stk_h * (i - stk_idx))

                start = stk_idx

            stk.append((h, start))
        
        
        last = len(heights)

        for h, idx in stk:

            largest_rect = max(largest_rect, h * (last - idx))
        
        return largest_rect