class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        """

              L M R
        0 1 2 3 4 5
        3 4 5 6 1 2  
        
          R
          L       
        0 1 2 3 4 5
        3,5,6,0,1,2 

        if mid == target:

            return mid                     

        elif L < mid:

            if L <= target <= mid:

                R = mid - 1  
            
            else:

                L = mi + 1

        else:

            L = mid + 1
                R
                L M R
        0 1 2 3 4 5 6
        4,5,6,7,0,1,2

        L M R 
        0 1 2
        5,1,3

        M
        L R
        0 1
        3 1


        """

        L = 0 
        R = len(nums) - 1

        while L <= R:

            mid = (L + R) // 2

            if nums[mid] == target:
                return mid

            elif nums[L] <= nums[mid]:

                if nums[L] <= target <= nums[mid]:

                    R = mid - 1 
                
                else:

                    L = mid + 1
            
            else:

                if nums[mid] <= target <= nums[R]:
                    L = mid + 1

                else:

                    R = mid - 1 

        return -1 