class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        
        ammendedList = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                ammendedList.append(0)
            else:
                ammendedList.append(1)
        ammendedList = sorted(ammendedList)
        return ammendedList
