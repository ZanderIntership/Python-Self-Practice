class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        
        sumT = 0
        for I in range(len(nums)):
            if I % 2 == 0:
                sumT += nums[I]
            else:
                sumT -= nums[I]

        return sumT
