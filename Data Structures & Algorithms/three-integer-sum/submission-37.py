class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        """
        output = list of lists where each sublist is contains nums[i] + nums[j] + nums[k] == 0
        nums[i] can be -ve or +ve or 0

        Brute Force:
        Triple loop approach = O(n**4)
        Sort = O(nlogn)
        0  1.  2 3 4 5
        -4 -1 -1 0 1 2

        [[-1,-1,2], 

        - For every number use as an anchor and do a two pointer squezze technique.

        Skip duplicates at the anchor level as well.

        - While L < R:
             if we found a triplet
                L += 1
                R += 1

                while L < R and nums[i-1] == nums[i]:
                    L += 1
                while L < and nums[i+1] == nums[i]:
                    R += 1 

        

        """
        res = []
        nums.sort()
        n = len(nums)

        for i, a in enumerate(nums):

            if a > 0:
                break
            
            #skipping duplicates at anchor level
            if i > 0 and a == nums[i-1]:
                continue
            
            L = i + 1
            R = n - 1

            while L < R:

                summ = a + nums[L] + nums[R]

                if summ == 0:
                    res.append([a,nums[L],nums[R]])
                    L += 1
                    R -= 1

                    while L < R and nums[L] == nums[L-1]:
                        L += 1

                    while L < R and nums[R] == nums[R+1]:
                        R -= 1

                elif summ > 0:
                    R -= 1

                else:
                    L += 1

        return res 


            

            
