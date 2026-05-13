class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #triple loop TC: O(n3) Not effecient

        #[-1,0,1,2,-1,-4]
        #sorted = [-4,-1,-1,0,1,2]
        
        triplets = []

        nums.sort()

        for i, a in enumerate(nums):

            #if anchor is positive the resulting sum will never be negetive
            if a > 0:
                break

            #skipping duplicates with anchor
            if i > 0 and a == nums[i-1]:
                continue
            
            L = i + 1
            R = len(nums) - 1

            while L < R:

                if nums[L] + nums[R] + a == 0:

                    triplets.append([a, nums[L], nums[R]])

                    #skipping duplicates in two sum problem
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1

                    L += 1
                    R -= 1
                
                elif nums[L] + nums[R] + a > 0:
                    R -= 1
                
                else:
                    L += 1
            
        return triplets

            


