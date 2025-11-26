class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        countChar = 0
        CountSpaces = 0
        AmmendedWord = ""
        for I in range(len(s)):
            countChar += 1
            if s[I] == " ":
                CountSpaces += 1
            if CountSpaces == k:
                break

        for J in range(0,countChar):
            AmmendedWord += s[J]
            # print(s[J], end = "") 

        return AmmendedWord.strip()
