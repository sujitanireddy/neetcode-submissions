class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)

        L = 0 
        R = m

        while L <= R:

            left_partition_point = (L + R) // 2
            right_partition_point = (m + n + 1) // 2 - left_partition_point

            nums1_left_max = float('-inf') if left_partition_point == 0 else nums1[left_partition_point - 1]
            nums1_right_min = float('inf') if left_partition_point == m else nums1[left_partition_point]

            nums2_left_max = float('-inf') if right_partition_point == 0 else nums2[right_partition_point - 1]
            nums2_right_min = float('inf') if right_partition_point == n else nums2[right_partition_point]


            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:

                if (m + n) % 2 == 0:

                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min )) / 2
                
                else:

                    return max(nums1_left_max, nums2_left_max)
            
            if nums2_left_max > nums1_right_min:

                L = left_partition_point + 1 

            else:

                R = left_partition_point - 1
                



        