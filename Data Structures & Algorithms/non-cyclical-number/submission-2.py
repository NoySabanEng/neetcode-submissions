class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n not in seen:
            seen.add(n)
            n = self.calcsum(n)
            if n == 1:
                return True
            
        return False

    def calcsum(self, n: int) -> int:
        dsum = 0
        while n:
            digit = n % 10
            n = n // 10
            dsum+= digit ** 2

        return dsum
