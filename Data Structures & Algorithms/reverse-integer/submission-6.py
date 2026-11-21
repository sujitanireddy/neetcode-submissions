class Solution:
    def reverse(self, x: int) -> int:
        sign = 0
        if x < 0:
            sign = -1

        res = int(str(abs(x))[::-1])

        if not (-(2**31) <= res <= (2**31 - 1)):
            return 0

        return res * sign if sign == -1 else res