class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        #We need to binary search on the smaller array. If nums2 is smaller moving it to nums1
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        L = 0 
        R = m

        while L <= R:

            nums1_partition = (L + R) // 2 
            nums2_partition = ((m + n + 1) // 2) - nums1_partition

            nums1_left_max = float('-inf') if nums1_partition == 0 else nums1[nums1_partition - 1]
            nums1_right_min = float('inf') if nums1_partition == m else nums1[nums1_partition]

            nums2_left_max = float('-inf') if nums2_partition == 0 else nums2[nums2_partition - 1]
            nums2_right_min = float('inf') if nums2_partition == n else nums2[nums2_partition]
            

            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:

                if (m + n) % 2 == 0:

                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
                
                else:

                    return max(nums2_left_max, nums1_left_max)
            
            if nums2_left_max > nums1_right_min:
                L = nums1_partition + 1
            
            else:
                R = nums1_partition - 1