class Solution:
    def reverse(self, x: int) -> int:
        
        def length(n):
            base = 0
            while n // 10 != 0:
                n = n//10
                base += 1
            return base
        
        def recurse(n, base):
            
            if n//10 == 0:
                return n

            return ((n % 10) * (10 ** base)) + recurse(n // 10, base - 1)
        
        sign = 1
        if x < 0:
            sign = -1
        
        base = length(abs(x))
        res = recurse(abs(x), base) * sign

        if -2**31 <= res <= ((2**31) - 1):
            return res
        else:
            return 0
