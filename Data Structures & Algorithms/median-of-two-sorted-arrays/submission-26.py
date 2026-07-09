class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        """
        median = middle most value. If even = 2 middle most values / 2
        O(log) = Binary search 

     0     1     2      3       4     5
        4     5     8   |   7      11   


      L    M            R
      0    1      2     3
        2  |  12    15

    
        2,4,5,7,8,11,12,15,16

        - Binary search on the smallest array of the both
        - Find cut points and validate thier eligibility 
        - Find median

        """

        if len(nums1) > len(nums2):
            nums2, nums1 = nums1, nums2

        m = len(nums1)
        n = len(nums2)

        L = 0 
        R = m

        while L <= R:

            nums1_left_numbers = (L + R) // 2
            print(nums1_left_numbers)
            print(m,n)
            nums2_left_numbers = ((m + n + 1) // 2) - nums1_left_numbers
            print(nums2_left_numbers)
            nums1_left_max = float("-inf") if nums1_left_numbers == 0 else nums1[nums1_left_numbers - 1]
            print(nums1_left_max)
            nums1_right_min = float("inf") if nums1_left_numbers == m else nums1[nums1_left_numbers]
            print(nums1_right_min)

            nums2_left_max = float("-inf") if nums2_left_numbers == 0 else nums2[nums2_left_numbers - 1]
            print(nums2_left_max)
            nums2_right_min = float("inf") if nums2_left_numbers == n else nums2[nums2_left_numbers]
            print(nums2_right_min)

            if nums1_left_max <= nums2_right_min and nums1_right_min >= nums2_left_max:
                if (m + n) % 2 == 0:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
                else:
                    return max(nums1_left_max, nums2_left_max)
            
            elif nums1_left_max > nums2_right_min:
                R = nums1_left_numbers - 1
            
            else:
                L = nums1_left_numbers + 1
        



