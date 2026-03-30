class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)

        #building left max array
        left_max = [0] * length
        left_max_so_far = 0
        for i in range(1, length):
            left_max_so_far = max(left_max_so_far, height[i-1])
            left_max[i] = left_max_so_far
        
        #building right max array
        right_max = [0] * length
        right_max_so_far = 0
        for j in range(length - 2, -1, -1):
            right_max_so_far = max(right_max_so_far, height[j+1])
            right_max[j] = right_max_so_far

        #computing water trapped at each index
        water_trapped_at_each_index = []
        for i in range(length):
            water_trapped = min(left_max[i], right_max[i]) - height[i]
            if water_trapped < 0:
                water_trapped_at_each_index.append(0)
            else:
                water_trapped_at_each_index.append(water_trapped)
        return sum(water_trapped_at_each_index)