class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        NewCandies = []
        Output = []

        temp = max(candies)
    

        for I in range(len(candies)):
            NewCandies.append(candies[I] + extraCandies) 

        for I in range(len(NewCandies)):
            if NewCandies[I] >= temp:
               Output.append(True)
            else:
                 Output.append(False)
        return Output
