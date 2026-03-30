class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        possible_areas = heights.copy()

        for i in range(len(heights)):

            l = float("inf")

            for j in range(i+1, len(heights)):

                l = min(l, heights[j], heights[i])
                b = (j - i) + 1
                possible_areas.append(l*b)

        return max(possible_areas)

        