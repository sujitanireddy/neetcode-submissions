class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_consecutive_seq = 0
        nums_set = set(nums)
    
        for n in nums:
            if (n - 1) not in nums_set:   #if no, then start of a seq
                curr_seq = 0
                while curr_seq + n in nums_set:
                    curr_seq += 1
                longest_consecutive_seq = max(longest_consecutive_seq, curr_seq)
        
        return longest_consecutive_seq