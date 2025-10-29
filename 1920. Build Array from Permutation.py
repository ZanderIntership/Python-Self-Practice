class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []

        for I in range(len(nums)):
            
            ans.append(nums[nums[I]])
        
        return ans
