"""
TC: O(n)
SC: O(n)

[9,9,9]

int ("999") = 999 + 1 = 1000
[ 1, 0, 0 , 0]

"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        output = []

        value = ""
        for digit in digits:
            value += str(digit)
        
        value = str(int(value) + 1)

        for val in value:
            output.append(int(val))

        return output