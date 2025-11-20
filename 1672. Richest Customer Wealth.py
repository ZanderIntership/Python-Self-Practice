class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        TotalWealth = []
        columnLength = len(accounts[0])
        UpKeep = 0

        for I in range(len(accounts)):
            for J in range(columnLength):
                UpKeep += accounts[I][J]

            TotalWealth.append(UpKeep)
            UpKeep = 0

        result = max(TotalWealth)
        return result
