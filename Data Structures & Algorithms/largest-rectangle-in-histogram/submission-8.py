class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stk = []
        n = len(heights)
        max_area = 0

        for i, h in enumerate(heights):

            #to keep track of start of the rect
            start = i

            while stk and h < stk[-1][0]:

                popped_h, popped_i = stk.pop()

                max_area = max(max_area, popped_h * (i - popped_i))

                start = popped_i

            stk.append((h, start))


        while stk:

            popped_h, popped_i = stk.pop()

            max_area = max(max_area, popped_h * (n - popped_i))
        
        return max_area

        