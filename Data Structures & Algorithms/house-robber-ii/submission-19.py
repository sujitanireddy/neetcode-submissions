class Solution:
    def rob(self, nums: List[int]) -> int:
        
        nums1 = nums[1:]
        nums2 = nums[:len(nums) - 1]

        def dfs(i, arr):

            if i in cache:
                return cache[i]

            if i >= len(arr):
                return 0

            cache[i] = max(arr[i] + dfs(i+2, arr), dfs(i+1, arr))

            return cache[i]

        cache = {}
        res1 = dfs(0,nums1)

        cache = {}
        res2 = dfs(0, nums2)

        return max(res1, res2, nums[0])