class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        longest_seq = 0

        for num in nums:
            #num is start of a seq
            if (num - 1) not in nums_set:

                longest_seq_by_far = 0

                while (num + longest_seq_by_far) in nums_set:

                    longest_seq_by_far += 1

                longest_seq = max(longest_seq, longest_seq_by_far)
        
        return longest_seq

