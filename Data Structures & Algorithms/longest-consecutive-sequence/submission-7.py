class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        longest_seq_len = 0

        for num in nums_set:

            if num - 1 not in nums_set: #this means that num is the start of a seq 

                seq_length = 1 #this counter captures the seq_length each start of seq found

                while (num + seq_length) in nums_set:

                    seq_length += 1

                longest_seq_len = max(longest_seq_len, seq_length)
        
        return longest_seq_len



                
        

        


        