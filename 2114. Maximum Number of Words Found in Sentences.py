class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        Spaces = 0
        SpaceContainer = []
        newWord = 0
        for I in range(len(sentences)):
            Spaces = 0
            newWord = sentences[I]
            for J in range(len(sentences[I])):
                if newWord[J] == ' ':
                    Spaces += 1
            Spaces += 1
            SpaceContainer.append(Spaces)

        return max(SpaceContainer)
            
