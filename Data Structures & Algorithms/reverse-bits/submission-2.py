class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if n & 1 == 1:
                bit = 1
            else:
                bit = 0
            n = n >> 1

            res += bit << (31 - i)
    
        return res