class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        TotalProduct = 1
        ToalSum = 0

        str_nValue = str(n)
        for I in range(0,len(str_nValue)):
            TotalProduct = TotalProduct * int(str_nValue[I])
            ToalSum += int(str_nValue[I]) 

        return TotalProduct - ToalSum
