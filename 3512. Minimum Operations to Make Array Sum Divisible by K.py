class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        sums = 0
        steps = 0

        for i in range(len(nums)):
            sums += nums[i]

        while sums % k != 0:
            r = sums % k
            if r > k / 2:
                Increment = k - r
                steps += Increment
                sums -= Increment
            elif r < k / 2:
                Increment = r
                steps += Increment
                sums -= Increment
            elif r == k /2:
                Increment = k - r
                steps += Increment
                sums -= Increment


        return steps

            
