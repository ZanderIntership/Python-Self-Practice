class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        Word_last = s.split()[-1]

        return len(Word_last)
