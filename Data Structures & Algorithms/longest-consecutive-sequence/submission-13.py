class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        longest_seq = 0

        for num in nums:

            if num - 1 not in nums_set:

                longest_seq_so_far = 0

                while (num + longest_seq_so_far) in nums_set:

                    longest_seq_so_far += 1

                longest_seq = max(longest_seq_so_far, longest_seq)
        
        return longest_seq


        