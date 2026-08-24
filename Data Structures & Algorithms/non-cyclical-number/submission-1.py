class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while True:
            seen.add(n)
            dsum = 0
            while n:
                digit = n % 10
                n = n // 10
                dsum+= digit ** 2

            if dsum == 1:
                return True
            elif dsum in seen:
                return False
            else:
                n = dsum
