class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stk = []
        max_area = 0

        for i, h in enumerate(heights):

            start = i

            while stk and stk[-1][1] > h:

                popped_idx, popped_h = stk.pop()

                max_area = max(max_area, (popped_h * (i - popped_idx)))

                start = popped_idx

            stk.append((start, h))

        end = len(heights)

        for idx, height in stk:

            max_area = max(max_area, height * (end - idx))

        return max_area