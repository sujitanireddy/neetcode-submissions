"""
[2,20,4,10,3,4,5] : Convert to set

{2,20,4,10,3,4,5}
             i

seq = 3

is nums[i-1] not in sett:
4

"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = set(nums)
        longest_seq = 0

        for i in range(len(nums)):

            seq = 1

            if nums[i] - 1 not in hashset:

                while seq + nums[i] in hashset:

                    seq += 1
            
            longest_seq = max(longest_seq, seq)
        
        return longest_seq
