class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for I in range(len(nums)):
            for J in range(len(nums)):
                if nums[I] == nums[J] and I < J:
                    count += 1

        return count
