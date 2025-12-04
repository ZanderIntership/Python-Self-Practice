class Solution:
    def addDigits(self, num: int) -> int:
        
        ArrayNum = []
        IndexArr = []
        NEwInt = str(num)
        ReplaceNum = num
        while len(NEwInt) > 1:

            ReplaceNum = 0
            
            for I in range(len(NEwInt)):
                ArrayNum.append(NEwInt[I])
                

            for I in range(len(NEwInt)):
                ReplaceNum += int(ArrayNum[I])
            
            NEwInt = str(ReplaceNum)
            
            ArrayNum = []


        
        return ReplaceNum
