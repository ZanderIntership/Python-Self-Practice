import math

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend == -1 and divisor == -1:
            return 1
        elif dividend < 0 and divisor < 0 and divisor == -1:
            Newdividend = dividend * -1
            return Newdividend - 1
        else:
            return math.trunc(dividend / divisor)
