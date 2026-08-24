class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while True:
            seen.add(n)
            digits = []
            while n:
                digit = n % 10
                n = n // 10
                digits.append(digit)
                
            dsum = 0
            for d in digits:
                dsum+= d ** 2

            if dsum == 1:
                return True
            elif dsum in seen:
                return False
            else:
                n = dsum
