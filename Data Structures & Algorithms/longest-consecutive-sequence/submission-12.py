class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        longest_seq = 0


        for i in range(len(nums)):

            if nums[i] - 1 not in nums_set:

                length = 1

                while (nums[i] + length) in nums_set:
                    
                    length += 1

                longest_seq = max(longest_seq, length)

        return longest_seq 



        