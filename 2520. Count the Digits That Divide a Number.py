class Solution:
    def countDigits(self, num: int) -> int:
        
        numString = str(num)
        CheckArray = []
        count = 0


        for I in range(len(numString)):
            CheckArray.append(int(numString[I]))

        
        for J in range(len(numString)):
            if num % CheckArray[J] == 0:
                count += 1

        return count
