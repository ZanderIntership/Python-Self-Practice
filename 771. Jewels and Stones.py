class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """

        count = 0
        for I in range(len(stones)):
            for J in range(len(jewels)):
                if stones[I] == jewels[J]:
                    count +=1

        return count
