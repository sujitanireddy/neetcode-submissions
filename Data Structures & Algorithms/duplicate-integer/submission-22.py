class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        sett = set()

        for number in nums:
            if number in sett:
                return True
            else:
                sett.add(number)

        return False
        