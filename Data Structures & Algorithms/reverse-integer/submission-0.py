class Solution:
    def reverse(self, x: int) -> int:

        def length_of_digits(n):
            counter = 0
            while n // 10 != 0:
                n = n // 10
                counter += 1
            return counter

        def reverse_recursion_pure(n, base):
            if n % 10 == n:
                return n
            rem = n % 10
            return (rem * (10 ** base)) + reverse_recursion_pure(n // 10, base - 1)

        sign = -1 if x < 0 else 1
        n = abs(x)
        base = length_of_digits(n)
        result = sign * reverse_recursion_pure(n, base)

        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if result < INT_MIN or result > INT_MAX:
            return 0

        return result
            