"""
1234

1234 // 10 = 4
123 // 10 = 3
12 // 10 = 2
1 // 10 = 0

1234 % 10 : 123

4000
 300
  20
   1
4321

f(i) = (i // 10) * (10 ** base) + f(i%10, base - 1)
"""
class Solution:
    def reverse(self, x: int) -> int:
        
        def length_of_digits(n):
            counter = 0
            while n != 0:
                n = n // 10
                counter += 1
            return counter
        
        def reverse(n, base):
            
            if n % 10 == n: return n

            return ((n % 10) * (10 ** base)) + (reverse(n//10, base - 1))

        n = abs(x)
        base = length_of_digits(n)
        res = reverse(n, base-1)

        if x < 0:
            res = -res
        
        if -2**31 <= res <= 2**31:
            return res

        return 0