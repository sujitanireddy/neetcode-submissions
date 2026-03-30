class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        #we always want to orperate on the smaller array consistently
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        L = 0
        R = m #we are looking for the partition point. So we might also encounter a scenario where there are 0 right elements 

        while L <= R:

            nums1_left_numbers = (L + R) // 2
            nums2_left_numbers = ((m + n + 1) // 2) - nums1_left_numbers

            print(nums1_left_numbers)

            nums1_left_max = float("-inf") if nums1_left_numbers == 0 else nums1[nums1_left_numbers - 1]
            nums1_right_min = float("inf") if nums1_left_numbers == m else nums1[nums1_left_numbers]

            nums2_left_max = float("-inf") if nums2_left_numbers == 0 else nums2[nums2_left_numbers - 1]
            nums2_right_min = float("inf") if nums2_left_numbers == n else nums2[nums2_left_numbers]

            
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:

                if (m + n) % 2 == 0:

                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
                
                else:

                    return max(nums1_left_max, nums2_left_max)
            
            if nums1_left_max > nums2_right_min:

                R = nums1_left_numbers - 1
            
            else:

                L = nums1_left_numbers + 1


