class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        PowerOfThree = 3
        while n >= 0:

            if n == 0:
                return True
            elif n % 3 == 2:
                return False
            elif n % 3 == 1:
                n = n // 3
            elif n % 3 == 0:
                n = n // 3

        return False
