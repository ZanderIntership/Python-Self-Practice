class Solution:
    def interpret(self, command: str) -> str:
        
        NewWord = command.replace("()", "o")
        NewWord = NewWord.replace("(al)", "al")

        return NewWord
