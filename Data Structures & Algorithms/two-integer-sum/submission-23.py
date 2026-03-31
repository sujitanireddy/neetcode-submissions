class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #Alorithm 
        #For every num in nums if target - num already in dict then return
        #the number's index with the current number's idx we are at.
        #Keep adding the current num to the set with it's index


        seen = defaultdict(int)

        for i in range(len(nums)):

            if target - nums[i] in seen:

                return [seen[target - nums[i]], i]
            
            seen[nums[i]] = i
        