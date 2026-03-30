class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range (0, len(numbers)):

            number_to_search = target - numbers[i]

            if number_to_search in numbers:

                return [i+1, numbers.index(number_to_search) + 1]