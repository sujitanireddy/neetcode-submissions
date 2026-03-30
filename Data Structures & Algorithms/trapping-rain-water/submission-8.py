class Solution:
    def trap(self, height: List[int]) -> int:
    
        #water_trapped = min(left_bound, right_bound) * (R - L) - 1 - h
        #[0,2,0,3,1,0,1,3,2,1]
        
        n = len(height)
        left_bound = [0] * n
        right_bound = [0] * n

        #[0,0,2,2,3,3,3,3,3,3]
        left_max_so_far = 0
        left_bound[0] = 0 
        for i in range(1, len(height)):
            left_max_so_far = max(left_max_so_far, height[i-1])
            left_bound[i] = left_max_so_far
        
        print(f"left_bound: {left_bound}")

        right_max_so_far = 0
        right_bound[-1] = 0
        #[0,2,0,3,1,0,1,3,2,1]
        #[3,3,3,3,3,3,3,2,1,0]
        for i in range(len(height)- 2, -1, -1):
            right_max_so_far = max(right_max_so_far, height[i+1])
            right_bound[i] = right_max_so_far
            
        print(f"right_bound: {right_bound}")
        print(f"height: {height}")

        water_trapped_by_far = 0
        for i in range(len(height)): 
            water_trapped = (min(left_bound[i], right_bound[i])) - height[i]

            if water_trapped > 0:
                water_trapped_by_far += water_trapped

        return water_trapped_by_far
            
        

            







