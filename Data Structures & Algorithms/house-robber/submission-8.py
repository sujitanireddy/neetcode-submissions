"""
Notes:
- Cannot rob two adj houses

              1      1
            3       3
-------------------------------------------
Recursion (BruteForce)

Basecase: if n >= len(nums)
f(n) = max(nums[n] + f(n+2), f(n+1))

 0 1 2 3 4
[2,9,8,3,6]

          n = 0: max(2 + f(2), f(1))
          n = 2: max(8 + 6, f(3))

TC: O(2**n)
SC: O(h)
-------------------------------------------
Top Down : Memoize

Map to store out compute and recuse it.
TC: O(n)
SC: O(n)
-------------------------------------------
Bottom up: DP Sol

i 
0 1 2 3 4
2,9,8,3,6

rob1  rob2  temp
0      0     0 
0      0     2
9      0     9

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1, rob2 = 0, 0

        for i in range(len(nums)):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

