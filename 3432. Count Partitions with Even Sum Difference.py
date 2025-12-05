class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        Partion1nums = nums
        StartingValue = Partion1nums[0]
        Partion2nums = [StartingValue]

        Partion1nums.pop(0)

        Total = 0
        EvenNumber = 0
        MinusAmount = 0
        while len(Partion1nums) >= 1:
            for I in range(len(Partion2nums)):
                Total += Partion2nums[I]

            # for J in range(len)

            for J in range(len(Partion1nums)):
                MinusAmount += Partion1nums[J]

            if (Total - MinusAmount) % 2 == 0:
                EvenNumber += 1
            else :
                pass

            Partion2nums.append(Partion1nums[0])
            Partion1nums.pop(0)
            Total = 0
            MinusAmount = 0
            
        return EvenNumber 

        

        
