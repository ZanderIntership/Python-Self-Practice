class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        Accumilation = 0
        for I in range(len(nums)):

            Accumilation += nums[I]
            output.append(Accumilation)

        return output
