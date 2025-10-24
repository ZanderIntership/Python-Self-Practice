class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        Year = int(date[:4])
        Month = int(date[5:7])
        Day = int(date[8:10])

        BinaryYear = bin(Year)[2:]
        BinaryMonth = bin(Month)[2:]
        BinaryDay = bin(Day)[2:]

        BinaryString = f"{BinaryYear}-{BinaryMonth}-{BinaryDay}"
        return BinaryString
        
