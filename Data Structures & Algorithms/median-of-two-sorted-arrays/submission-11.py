class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):

            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        
        #binary search 
        L = 0
        R = m

        while L < R:

            nums1_left_elements = (L + R) // 2
            nums2_left_elements = ((m + n + 1) // 2) - nums1_left_elements

            nums1_left_max = float("-inf") if nums1_left_elements == 0 else nums1[nums1_left_elements - 1]
            nums1_right_min = float("inf") if nums1_left_elements == m else nums1[nums1_left_elements]

            nums2_left_max = float("-inf") if nums2_left_elements == 0 else nums2[nums2_left_elements - 1]
            nums2_right_min = float("inf") if nums2_left_elements == n else nums2[nums2_left_elements]

            if nums1_left_max  <= nums2_right_min and nums2_left_max <= nums1_right_min:

                if (m + n) % 2 == 0:

                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2 
                
                else:

                    return max(nums1_left_max, nums2_left_max)
            
            if nums2_left_max > nums1_right_min:

                L = nums1_left_elements + 1
            
            else:

                R = nums1_left_elements - 1


            





