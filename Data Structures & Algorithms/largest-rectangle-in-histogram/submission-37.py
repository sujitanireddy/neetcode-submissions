class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_area = 0
        stk = []

        for i, h in enumerate(heights):

            stk_idx = i

            while stk and h < stk[-1][0]:

                stk_h, stk_idx = stk.pop()

                largest_area = max(largest_area, stk_h * (i - stk_idx))

            stk.append((h, stk_idx)) #height, idx

        R = len(heights)
        for h, i in stk:
            largest_area = max(largest_area, h * (R - i))
        
        return largest_area
