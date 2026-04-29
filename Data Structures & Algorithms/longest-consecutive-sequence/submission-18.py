class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)

        longest = 0 
        
        for num in nums:

            if (num - 1) not in nums_set: #start of a sequence

                seq = 0

                while (num + seq) in nums_set:

                    seq += 1
            
                longest = max(longest, seq)

        return longest


