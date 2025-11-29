class Solution:
    def removeStars(self, s: str) -> str:
        
    
        Kept = []
        for i in range(len(s)):
            if s[i] == "*" :
                Kept.pop()
            else:
                Kept.append(s[i])
                    
        return "".join(Kept)
