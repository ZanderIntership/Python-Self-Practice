class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort(reverse = False)

        difference = 0
        for I in range(len(nums) - 1):
            if nums[I + 1] - nums[I] >  difference:
                difference = nums[I + 1] - nums[I]
        return difference 
