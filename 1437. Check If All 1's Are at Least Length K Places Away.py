class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        Locations = []
        Spacing = 0


        for I in range(len(nums)):
            if nums[I] == 1:
                Locations.append(I)
        
        if len(Locations) < 1:
            return True

        for I in range(len(Locations) - 1):
            if (Locations[I + 1] - Locations[I]) - 1 >= k:
                Spacing += 1

        if Spacing == len(Locations ) - 1:
            
            return True
        elif k == 0:
            return True
        else:
            return False

        # return Locations



        return Locations
