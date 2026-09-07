class Solution:
    def reverse(self, x: int) -> int:
        if -9 <= x <= 9:
            return x

        def calculate_base(n):
            base = 0

            while n // 10 != 0:
                n = n // 10
                base += 1

            return base

        def reverse(n, base):

            if base == 0:
                return n

            return (n % 10) * (10**base) + reverse(n // 10, base - 1)

        sign = 1
        if x < 0:
            sign = -1

        base = calculate_base(abs(x))
        reversed_int = reverse(abs(x), base)
        if (-(2**31)) <= reversed_int <= ((2**31) - 1):
            return reversed_int * sign
        else:
            return 0
