class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest_seq_so_far = 0

        nums_set = set(nums)

        for num in nums:

            if (num - 1) in nums_set:
                continue
            
            longest_seq = 1
            
            while (num + longest_seq) in nums_set:
                
                longest_seq += 1

            longest_seq_so_far = max(longest_seq_so_far, longest_seq)
        
        return longest_seq_so_far


