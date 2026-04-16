class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()

        n = len(nums1) - 1
        l, r  = 0, n

        if n/2 != 1:
            mid = (l + r) // 2
            meidan = (nums1[mid] + nums1[mid+1]) / 2
            return meidan

        else:    
            meidan = (nums1[l] + nums1[r]) / 2
            return meidan
        