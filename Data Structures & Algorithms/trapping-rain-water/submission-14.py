class Solution:
    def trap(self, height: List[int]) -> int:
        
        """
        left and right boundries

        What if we pre-compute the left and right boundries? 

        height =      [0,2,0,3,1,0,1,3,2,1]
        left_bound =  [0,0,2,2,3,3,3,3,3,3]
        right_bound = [3,3,3,3,3,3,3,2,1,0]
        water_stored= min(right_bound, left_bound) - height[i]

        """

        max_area = 0
        n = len(height)
        left_bound = [0] * n
        right_bound = [0] * n

        #Compute left_bound
        left_max = 0
        for i in range(1, n):
            left_max = max(left_max, height[i-1])
            left_bound[i] = left_max
        print(left_bound)
            
        #Compute right_bound
        right_max = 0
        for i in range(n - 2, -1, -1):
            right_max = max(right_max, height[i+1])
            right_bound[i] = right_max
            
        print(right_bound)
        
        for i in range(n):
            area = min(left_bound[i], right_bound[i]) - height[i]
            if area > 0:
                max_area += area
        
        return max_area

        


