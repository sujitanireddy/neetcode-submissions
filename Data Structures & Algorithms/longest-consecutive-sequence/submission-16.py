class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        nums_set = set(nums)

        for num in nums:

            if (num - 1) not in nums_set:

                longest_so_far = 0

                while (num + longest_so_far) in nums_set:

                    longest_so_far += 1
                
                longest = max(longest, longest_so_far)
        
        return longest

