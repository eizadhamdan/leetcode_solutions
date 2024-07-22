class Solution:
    def repeatedCharacter(self, s: str) -> str:
        freq = {}

        for letter in s:
            if letter not in freq:
                freq[letter] = 1
            else:
                return letter
            