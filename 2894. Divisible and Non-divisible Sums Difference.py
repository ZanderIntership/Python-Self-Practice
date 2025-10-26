class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
        num1 = 0
        num2 = 0

        for I in range (1,n + 1):
            if I % m != 0:
                num1 = num1 + I
            elif I % m == 0:
                num2 = num2 + I    


        return num1 - num2
