class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringx = str(x)
        EndOFString = len(stringx)
        Total = EndOFString
        Palidrome = False
        CountCorrect = 0

        I = 0
        for I in range(len(stringx)):
            if stringx[I] == stringx[EndOFString - 1]:
               CountCorrect += 1
            else:
                CountCorrect = CountCorrect
            EndOFString -= 1

        if CountCorrect == Total :
            Palidrome = True
            return Palidrome
        else:
            Palidrome = False
            return Palidrome

        
  

        
        
