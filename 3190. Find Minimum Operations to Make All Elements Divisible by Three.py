class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        Counter = 0
        Devider = 0
        Step = 0
        while Counter != len(nums):
            Counter = 0
            for I in range(len(nums)):
                Devider = nums[I] % 3 
                if nums[I] % 3 != 0 and Devider == 2 :
                    Step += 1
                    nums[I] = nums[I] + 1
                elif nums[I] % 3 != 0 and Devider == 1:
                    Step += 1
                    nums[I] = nums[I] - 1
                elif nums[I] % 3 == 0:
                    Counter += 1
            

        return Step
