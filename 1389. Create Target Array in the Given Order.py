class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        NewArray = []

        for I in range(len(nums)):
            NewArray.insert(index[I],nums[I] )

        return NewArray
