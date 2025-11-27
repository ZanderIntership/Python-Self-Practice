class Solution:
    def sumOfMultiples(self, n: int) -> int:
        
        Accumulationarr = []
        Sum = 0

        for I in range(0,n + 1):
            if I % 3 == 0 or I % 5 == 0 or I % 7 == 0:
               Accumulationarr.append(I)

        for I in range(len(Accumulationarr)):
            Sum += Accumulationarr[I]

        return Sum
