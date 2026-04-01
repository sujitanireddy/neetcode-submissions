class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Algorithm 
        #Sort the input array in place
        #For every number in nums if num > 0: break
            #if i > 0 & num == num - 1: continue
            #L = i + 1 & R = len(nums) -1
            #Two pointer sqeeze technique and skip duplicates within twopointers 

        triplets = []
        nums.sort()

        print(nums)

        for i, a in enumerate(nums):

            #cannot be summing up to zero
            if a > 0:
                break
            
            #skipping duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            L = i + 1
            R = len(nums) - 1

            while L < R:

                if a + nums[L] + nums[R] == 0:
                    triplets.append([a, nums[L], nums[R]])
                    L +=1 
                    R -=1
                    
                    #skipping duplicates within two pointer sum
                    while L < R and nums[L] == nums[L-1]:
                        L +=1 
                    
                    while L < R and nums[R] == nums[R+1]:
                        R-=1
                
                elif a + nums[L] + nums[R] > 0:

                    R -= 1

                else:

                    L += 1
                
        return triplets
