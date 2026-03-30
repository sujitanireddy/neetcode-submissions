class Solution:
    def maxArea(self, heights: List[int]) -> int:

        result = 0
        
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):

                height = min(heights[i], heights[j])
                breath = j - i

                area = height * breath
                result = max(result, area)

        return result

            