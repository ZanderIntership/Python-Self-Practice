class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for I in range(1,len(s)):
            score += abs(ord(s[I]) - ord(s[I - 1]))

        return score
