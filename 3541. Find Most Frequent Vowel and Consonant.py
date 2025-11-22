class Solution:
    def maxFreqSum(self, s: str) -> int:


        consonants_map = {
    'b': 0, 'c': 0, 'd': 0, 'f': 0, 'g': 0,
    'h': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
    'n': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0,
    't': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
    }

        vowels_map = {
    'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0
    }


        for I in range(len(s)):
            letter = str(s[I]) 
            if letter in vowels_map:
                vowels_map[letter] += 1
            elif letter in consonants_map:
                consonants_map[letter] += 1
    
        MaxVlaueVowels = max(vowels_map.values())
        MaxValueConstants = max(consonants_map.values())

        return MaxVlaueVowels + MaxValueConstants

    


        

        
