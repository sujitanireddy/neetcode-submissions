class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stk = []
        max_area_so_far = 0

        for i, h in enumerate(heights):

            start = i

            while stk and h < stk[-1][1]:

                popped_idx, popped_height = stk.pop()

                area = popped_height * (i - popped_idx)

                max_area_so_far = max(max_area_so_far, area)

                start = popped_idx

            
            stk.append((start, h))


        length = len(heights)

        for i, h in stk:

            max_area_so_far = max(max_area_so_far, (h * (length - i)))


        return max_area_so_far