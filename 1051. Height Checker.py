class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        Predictons = heights.copy() 
        temp = 0
        Counter = 0

        for I in range(len(heights)):
            for J in range(len(heights)):
                if Predictons[I] < Predictons[J]:
                    temp = Predictons[I]
                    Predictons[I] = Predictons[J]
                    Predictons[J] = temp
            
        
        for I in range(len(heights)):
            if heights[I] != Predictons[I]:
                Counter += 1

        return Counter
        
