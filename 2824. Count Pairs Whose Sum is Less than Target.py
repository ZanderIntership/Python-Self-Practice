class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        

        pairs = 0
        for I in range(len(nums)):
            for J in range(len(nums)):
                if I < J:    
                    if nums[I] + nums[J] < target:
                        pairs+= 1

        return pairs
