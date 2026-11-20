class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        a, b = a & mask, b & mask
        carry = 0
        res = 0

        for i in range(32):
            a_bit = a & 1
            a = a >> 1

            b_bit = b & 1
            b = b >> 1

            bit = a_bit ^ b_bit ^ carry
            carry = (a_bit & b_bit) | (carry & (a_bit ^ b_bit))

            res = res | (bit << i)

        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)

        return res