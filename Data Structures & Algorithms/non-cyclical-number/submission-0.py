class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        def non_cyclical_number(val):

            res = 0

            if val in seen:
                return False
            
            if val == 1:
                return True
            
            seen.add(val)

            for n in str(val):
                res += (int(n)) ** 2

            return non_cyclical_number(res)
        
        return non_cyclical_number(n)
        

