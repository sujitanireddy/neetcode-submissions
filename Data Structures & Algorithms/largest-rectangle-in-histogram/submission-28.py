"""
 0 1 2 3 4 5
[7,1,7,2,2,4]

7   X     X   
6
5
4                  X
3
2            X  X  
1      X 
    1  2  3  4  5  6  7

Notes:
- My bottelneck is always the smaller height

#[(height, idx)]

[(1,0),(2,2),(2,4),(4,5)]

on stk save the index of the poped one.

while stk and stk[-1][0] > h:
    stk_h, stk_idx = stk.pop()

compute the area
[(1,0),(2,2),(2,4),(4,5)]
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stk = []
        largest_area = 0

        for i, h in enumerate(heights):

            stk_i = i

            while stk and stk[-1][0] > h:

                stk_h, stk_i = stk.pop()
            
                largest_area = max(largest_area, stk_h * (i - stk_i))  
            
            stk.append((h,stk_i))
        
        print(stk)

        
        length = len(heights)

        for h, i in stk:

            largest_area = max(largest_area, h * (length - i))
        
        return largest_area
        



"""
 0 1 2 3 4 5
[7,1,7,2,2,4]

[(1,0)]

(7,0)

"""
        