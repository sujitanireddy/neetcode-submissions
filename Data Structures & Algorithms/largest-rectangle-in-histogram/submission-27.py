class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        """
        bottleneck of h is always the lower height in the range

        [            (h,i)

        (7,0)

        if h < top of the stk (stk[-1][0]):
            pop

        area = stk_h * (i - stk_idx)
        """
        stk = []
        max_area = 0

        for i, h in enumerate(heights):

            stk_idx = i

            while stk and h < stk[-1][0]:

                stk_h, stk_idx = stk.pop()

                area = stk_h * (i - stk_idx)

                max_area = max(max_area, area)

            stk.append((h, stk_idx))

        length = len(heights)
        
        for h,i in stk:
            area = h * (length - i)
            max_area = max(max_area, area)

        return max_area

