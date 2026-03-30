class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stk = []
        max_area_so_far = 0

        for i, h in enumerate(heights):

            start = i

            while stk and stk[-1][0] > h:

                popped_height, popped_idx = stk.pop()

                L = popped_height
                B = i - popped_idx
                area = L * B

                max_area_so_far = max(max_area_so_far, area)

                start = popped_idx

            stk.append((h, start))
        
        for h, popped_idx in stk:

            i = len(heights)

            l = h
            b = i - popped_idx
            max_area_so_far = max(max_area_so_far, l*b)

        return max_area_so_far
            
