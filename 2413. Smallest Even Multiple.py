class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        TillTrue = True

        while TillTrue:
            if n % 2 == 0:
                TillTrue = False
                return n
            elif n % 2 == 1:
                TillTrue = True
                n *= 2
