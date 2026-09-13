"""

1 2 3 4 => 1 2 3 5 

if last digit is between 0 - 8: add one to last digit and return

[9,9,9] => 1 0  0  0

1 2 9 =>     1  3   0
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1, -1 ,-1):

            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            elif digits[i] == 9:
                digits[i] = 0
        
        return [1] + digits