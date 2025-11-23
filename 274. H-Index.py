class Solution:
    def hIndex(self, citations: List[int]) -> int:
        NewCitations = citations.copy()
        NewCitations.sort(reverse = True)
        
        index = 0
        stop = False
        for I in range(len(NewCitations)):
            if NewCitations[I] < I + 1 and stop == False:
                index = I 
                stop = True
            elif len(NewCitations) == 1 and stop == False:
                index = 1
                stop = True

        if stop == False:
            index = len(citations)

        return index 
