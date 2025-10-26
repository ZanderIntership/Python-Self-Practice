class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        
        count = 0
        DCounter = 0
        Duplication = []
        for I in range(len(nums)):
            for J in range(len(nums)):
                if nums[I] == nums[J]:
                    count = count + 1
            if count > 1 and nums[I] not in Duplication:
                Duplication.append(nums[I])
                DCounter += 1
            count = 0
        return Duplication
