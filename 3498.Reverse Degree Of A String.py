class Solution:
    def reverseDegree(self, s: str) -> int:
        alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        countdown = list(range(26, 0, -1))
        product = 0

        
        I2 = 1
        for I in range(len(s)):
            for J in range(len(alphabet)):
                if s[I] == alphabet[J]:
                    product += I2 * int(countdown[J])
                    I2 = I2 + 1

        return product
        
