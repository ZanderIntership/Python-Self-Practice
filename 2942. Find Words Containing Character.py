class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        cout = []
        found = False
        for I in range(len(words)):
            for J in range(len(words[I])):
                if x in words[I]:
                    found = True
            if found == True:
                cout.append(I)
                found = False

        return cout
