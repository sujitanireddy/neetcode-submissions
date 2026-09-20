"""
Binary serch = log(m+n)

nums1 = [1,3], nums2 = [2,4]

L   M   R

0   1   2   3

  2 | 4 

  1   3 |  5



1

1       |   5      8

2   4   | float("inf")


if nums1_left_max > nums2_right_min:
    R = mid + 1


1   2   3   4   5

1   2   4   5

1   2   4   5   8

left_side = +1 for odd numbers
binary serch on smaller array

if it's odd length then the median is to the left side

if it's even then take the average from left(max) and right(min)


"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        #Always binary search on nums1
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)
        L = 0
        R = m

        while L <= R:

            nums1_left_no = (L + R) // 2
            nums2_left_no = ((m + n + 1) // 2) - nums1_left_no

            nums1_left_max = float("-inf") if nums1_left_no == 0 else nums1[nums1_left_no - 1]
            nums1_right_min = float("inf") if nums1_left_no == m else nums1[nums1_left_no]

            nums2_left_max = float("-inf") if nums2_left_no == 0 else nums2[nums2_left_no - 1]
            nums2_right_min = float("inf") if nums2_left_no == n else nums2[nums2_left_no]

            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:

                if (m + n) % 2 == 0:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
                
                else:
                    return max(nums1_left_max, nums2_left_max)
            
            elif nums1_left_max > nums2_right_min:
                R = nums1_left_no - 1
            
            else:
                L = nums1_left_no + 1



"""
L   R
M
0   1    2
| 2


  1    3 |


-inf | 2
 3   | inf




"""
        








































        