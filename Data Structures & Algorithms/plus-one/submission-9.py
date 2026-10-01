"""
 0 1 2 3
[1,2,3,4]

1 2 3 

1 2 4 0

1 0 0 0

1 0

 0 0

0   0   0

Notes:
- If last digit is not 9. Just increment
- If it's 9, make it 0 
- if all digits are 9 then add [1] at the end

"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1, -1 ,-1):

            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            else:
                digits[i] = 0
        
        return [1] + digits