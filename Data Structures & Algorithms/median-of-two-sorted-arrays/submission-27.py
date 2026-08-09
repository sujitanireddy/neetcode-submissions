class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        """
        odd = middle most val
        even = avg of the 2 most middle vals

        Binary Search 

        - We will always bs on smaller arr
        - We will always make sure 1 extra element is in smaller arr

        left place holder = -inf
        right place holder = +inf
                 
                            M
                 L          R             
                 0 1        2 3 4
        
        nums1 =  5 6      | 7 8 
        nums2 =  11 18 19 | 20 21  
        
        [5,6,7,8,11,18,19,20,21]

        5 - 2 = 3

        """

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        L = 0
        R = m

        while L <= R:

            nums1_left_no = (L+R)//2
            nums2_left_no = ((m + n + 1) // 2) - nums1_left_no

            nums1_left_max = float("-inf") if nums1_left_no == 0 else nums1[nums1_left_no - 1]
            nums1_right_min = float("inf") if nums1_left_no == m else nums1[nums1_left_no]

            nums2_left_max = float("-inf") if nums2_left_no == 0 else nums2[nums2_left_no - 1]
            nums2_right_min = float("inf") if nums2_left_no == n else nums2[nums2_left_no]

            if nums1_left_max <= nums2_right_min and nums1_right_min >= nums2_left_max:
                if (m+n) % 2 == 0:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min))/ 2
                
                else: 
                    return max(nums1_left_max, nums2_left_max)

            elif nums1_left_max > nums2_right_min:
                R = nums1_left_no - 1

            else:
                L = nums1_left_no + 1









