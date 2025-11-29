class Solution:
    def numberOfMatches(self, n: int) -> int:
        SumMatches = 0

        while n != 1:
            
            if n % 2 == 0:
                SumMatches += (n // 2)
                n -= n // 2
                n = int(n)
            elif n % 2 == 1:
                SumMatches += (n // 2) 
                n -= (n // 2) - 0.5
                n = int(n)

            n = int(n)
        
        return SumMatches
