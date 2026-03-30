class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        left_max_prefix_array = [0] * n
        right_max_prefix_array = [0] * n

        left_max_so_far = 0
        for i in range(1, n):
            left_max_so_far = max(left_max_so_far, height[i-1])
            left_max_prefix_array[i] = left_max_so_far
        
        print(left_max_prefix_array)

        right_max_so_far = 0
        for i in range(n-2, -1, -1):
            right_max_so_far = max(right_max_so_far, height[i+1])
            right_max_prefix_array[i] = right_max_so_far
        
        print(right_max_prefix_array)

        water_trapped_so_far = 0
        for i in range(n):
            water_trapped = 0
            water_trapped = min(left_max_prefix_array[i], right_max_prefix_array[i]) - height[i]
            if water_trapped > 0:
                water_trapped_so_far += water_trapped

        return water_trapped_so_far



        