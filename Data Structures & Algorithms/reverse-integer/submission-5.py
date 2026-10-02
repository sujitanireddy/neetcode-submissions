"""
Brute Force: 
- int -> str -> reverse the string -> int -> check if it's out of bounds 

TC: O(n)
SC: O(n)

1   2   3   4


1234 // 10 = 123

1234 % 10 = 4

f(n) = (n % 10) ** 10 * (length - 1) + f(n//10)



4 0 0 0
  3 0 0
    2 0
      1  

1234 % 10 = 4
123 % 10 = 12
12 % 10 = 1
1 % 10 == 1? 

3

"""
class Solution:
    def reverse(self, x: int) -> int:
        
        def calculate_length(n):
            length = 0
            
            while n % 10 != n:
                length += 1
                n = n // 10
            
            return length

        
        def reverse(n, length):
            
            if n % 10 == n:
                return n
            
            return (n % 10) * (10 ** length) + reverse(n // 10, length - 1)


        sign = 1
        if x < 0:
            sign = -1
        
        length = calculate_length(abs(x))
        res = reverse(abs(x), length)
        res *= sign

        if (-2 ** 31) <= res <= (2 ** 31) - 1:
            return res
        else:
            return 0