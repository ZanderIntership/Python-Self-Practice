class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for I in range(len(nums)):
            ans.append(nums[I]) 

        for I in range(len(nums)):
            ans.append(nums[I])     

        return ans
