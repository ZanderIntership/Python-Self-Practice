class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        index = 0
        for I in range(len(word)):
            if word[I] == ch:
                if I == 0:
                    return word
                    exit()
                elif index < 1:
                    index = I
                
            

        start = 0

        Reversed = word[:start] + word[start:index + 1][::-1] + word[index + 1:]

        return Reversed
