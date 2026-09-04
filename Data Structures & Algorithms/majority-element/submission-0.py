"""
5

3.5 > 

[5,5,1,1,1,5,5]

{
  5 : 4
  1 : 3
}

"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        for key, value in freq.items():
            if value > (len(nums) / 2):
                return key