class Solution:
    def rob(self, nums: List[int]) -> int:

        def recurse(i, arr):

            if i >= len(arr):
                return 0
            
            if i in cache:
                return cache[i]
            
            cache[i] = max(arr[i] + recurse(i+2, arr), recurse(i+1, arr))

            return cache[i]

        if len(nums) == 1:
            return nums[0]

        cache = {}
        skip_house_one = [] 
        for i in range(1, len(nums)):
            skip_house_one.append(nums[i])

        res1 = recurse(0, skip_house_one)

        cache = {}
        skip_last_house = []
        for j in range(len(nums)-1):
            skip_last_house.append(nums[j])

        res2 = recurse(0, skip_last_house)

        return max(res1, res2)
        
        