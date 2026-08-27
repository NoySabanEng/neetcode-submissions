class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = res << 1
            res |= 1 if (n & (1 << i)) else 0
        return res

            
        