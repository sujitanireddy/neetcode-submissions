"""
[9,8,3,6]
[2,9,8,3]

Bruteforce: 
f(i) = max(nums[i] + f(i+2), f(i+1))

"""
class Solution:
    def rob(self, nums: List[int]) -> int:

        def recurse(i,arr):

            if i in cache:
                return cache[i]
            
            if i >= len(arr):
                return 0
            
            cache[i] = max(arr[i] + recurse(i+2,arr), recurse(i+1,arr))

            return cache[i]

        cache = {}
        skip_one = [nums[i] for i in range(1,len(nums))]
        res_1 = recurse(0, skip_one)

        cache = {}
        skip_last = [nums[i] for i in range(len(nums) - 1)]
        res_2 = recurse(0, skip_last)

        return max(nums[0], res_1, res_2)