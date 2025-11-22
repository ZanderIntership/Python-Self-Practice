class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        Position = []
        
        for I in range(k):
            Smallest = min(nums)
            for I in range(len(nums)):
                if Smallest == nums[I]:
                    Position.append(I)
            
            Firstposition = Position[0]

            NewNumber = nums[Firstposition] * multiplier

            nums[Firstposition] = (NewNumber)
            Position.clear()

        return nums

        
