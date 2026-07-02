class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_area = 0
        stk = [] #(index, height)

        for i, h in enumerate(heights):
            start = i

            while stk and stk[-1][1] > h:
                stk_i, stk_h  = stk.pop()
                max_area = max(max_area, stk_h * (i - stk_i))
                start = stk_i

            stk.append((start, h))

            
        length = len(heights)
        for i, h in stk:
            max_area = max(max_area, h * (length - i))   
        return max_area     

