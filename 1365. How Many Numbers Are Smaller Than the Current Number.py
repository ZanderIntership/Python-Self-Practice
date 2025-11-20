class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        RevisedArray = []
        Count = 0
        
        for I in range(len(nums)):
            for J in range(len(nums)):
                if J != I and nums[J] < nums[I]:
                    Count += 1
              
            RevisedArray.append(Count)
            Count = 0  
        return  RevisedArray
