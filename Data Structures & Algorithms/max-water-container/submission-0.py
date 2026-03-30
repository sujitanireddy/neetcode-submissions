class Solution:
    def maxArea(self, heights: List[int]) -> int:

        height = 0
        breath = 0
        area = float("-inf") 

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):

                height = min(heights[i], heights[j])
                breath = j - i
                temp_area = height * breath

                if temp_area > area:
                    area = temp_area
        return area
                

                
