class Solution:
    def hammingWeight(self, n: int) -> int:
        print(format(n, 'b'))  # Output: '1010'
        print(format(n, '#b'))  # Output: '1010'
        return bin(n).count("1")