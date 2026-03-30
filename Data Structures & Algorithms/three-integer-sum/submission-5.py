class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        triplets = []

        nums.sort()

        for i in range(len(nums) - 2):
            for j in range(i+1, len(nums) - 1):
                for k in range(j+1, len(nums)):

                    if nums[i] + nums[j] + nums[k] == 0:

                        if [nums[i], nums[j], nums[k]] in triplets:
                            continue
                        else:
                            triplets.append([nums[i], nums[j], nums[k]])
        
        return triplets
        
        


        