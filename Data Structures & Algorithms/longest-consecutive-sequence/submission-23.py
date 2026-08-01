class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        """
        [2,20,4,10,3,4,5]
        {2,20,4,10,3,4,5}

        longest = 4

        i = 4

        if there is 2-1 in the set then that is not the start.
        If there is not nums - 1 in the set that means that it's the start of a sequence.
        """
        longest = 0
        nums_set = set(nums)

        for num in nums:
            
            i = 0
            
            if (num - 1) not in nums_set:


                while (num + i) in nums_set:
                    i += 1
                    
            longest = max(longest, i)
        
        return longest