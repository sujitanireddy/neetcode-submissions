class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """
        hashamp = {4:0}

            {
                6 : 0
                5 : 1

            }

        """
        hashmap = defaultdict(int)

        for i in range(len(nums)):

            if nums[i] in hashmap:

                return [hashmap[nums[i]], i]
            
            hashmap[target - nums[i]] = i



            

            