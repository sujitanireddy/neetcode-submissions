class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        """
        #using a hashset
        (2,20,4,10,3,4,5)

        is 2 - 1 in the hashset? if not then it's start of a seq.

        """

        max_so_far = 0
        sett = set(nums)
        seq = 0

        for num in nums:

            if (num - 1) not in sett:

                seq = 0

                while (num + seq) in sett:

                    seq += 1
            
            max_so_far = max(max_so_far, seq)

        return max_so_far                


                 