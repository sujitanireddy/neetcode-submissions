class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        
        n = len(nums1)
        
        if n == 1:
            return float(nums1[0])
        
        if n % 2 == 0:  # even
            mid = n // 2
            return (nums1[mid - 1] + nums1[mid]) / 2
        else:  # odd
            mid = n // 2
            return float(nums1[mid])