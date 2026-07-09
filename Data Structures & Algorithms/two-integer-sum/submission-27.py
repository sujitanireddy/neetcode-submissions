class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """

        hashmap = { 4: 0 
                    }

        """

        hashmap = defaultdict() #{diffrence: idx}

        for i, num in enumerate(nums):

            if num in hashmap:
                return [hashmap[num], i]

            hashmap[target - num] = i
            

        
        
