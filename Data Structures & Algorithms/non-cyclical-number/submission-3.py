class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.calcsum(n)

        while slow != fast:
            fast = self.calcsum(fast)
            fast = self.calcsum(fast)
            slow = self.calcsum(slow)
        return True if fast == 1 else False

    def calcsum(self, n: int) -> int:
        dsum = 0
        while n:
            digit = n % 10
            n = n // 10
            dsum+= digit ** 2

        return dsum