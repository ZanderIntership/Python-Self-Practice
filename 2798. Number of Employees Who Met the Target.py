class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0

        for I in range(len(hours)):
            if target <= hours[I]:
                count += 1
 
        return count
