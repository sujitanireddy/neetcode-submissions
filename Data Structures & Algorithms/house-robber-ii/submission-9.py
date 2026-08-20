"""
[9,8,3,6]
[2,9,8,3]

Bruteforce: 
f(i) = max(nums[i] + f(i+2), f(i+1))

                 
                 9 8 3  6
                 9 8 
                 r2r1t
             

temp = max(nums[i] + r2, r1)
r2 = r1
r1 = temp
return r1

"""
class Solution:
    def rob(self, nums: List[int]) -> int:

        def find_max(arr):
            r1, r2 = 0, 0
            for i in range(len(arr)):
                temp = max(arr[i] + r1, r2)
                r1 = r2
                r2 = temp
            return r2

        skip_one = [nums[i] for i in range(1,len(nums))]
        res_1 = find_max(skip_one)

        skip_last = [nums[i] for i in range(len(nums) - 1)]
        res_2 = find_max(skip_last)


        print(res_1, res_2)

        return max(nums[0], res_1, res_2)