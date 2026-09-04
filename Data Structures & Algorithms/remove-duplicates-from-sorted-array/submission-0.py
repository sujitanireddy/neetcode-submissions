"""
[1,1,2,3,4]

{
  1 : 2
  2 : 1
  3 : 1
  4 : 1
}
TC : O(n)
SC:  O(n)
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        i = 0
        for key in freq.keys():
            nums[i] = key
            i += 1
        
        return len(freq)
