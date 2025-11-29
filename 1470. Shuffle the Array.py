class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arrayLeft = []
        arrayRight = []
        NewArray = []
        LeftCounter = n

        for I in range(n):
            arrayLeft.append(nums[I])

        for J in range(n):
            arrayRight.append(nums[LeftCounter])
            LeftCounter += 1

        for I in range(n):
            NewArray.append(arrayLeft[I])
            NewArray.append(arrayRight[I])

        return NewArray
