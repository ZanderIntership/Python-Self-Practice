class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        NewCosts = sorted(costs)
        Counter = 0

        for I in range(len(NewCosts)):
            if coins > NewCosts[I] or coins == NewCosts[I]:
                Counter += 1
                coins -= NewCosts[I]

        return Counter

