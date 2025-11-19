class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        for I in range(len(nums)):              
            for I in range(len(nums)):
                if original == nums[I]:
                    original = original * 2
        return original

        
   
