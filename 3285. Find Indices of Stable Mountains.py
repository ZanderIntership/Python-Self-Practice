class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        
        NewArray = []

        for I in range(1,len(height)):
            if height[I - 1] > threshold:
                NewArray.append(I)

        return NewArray
