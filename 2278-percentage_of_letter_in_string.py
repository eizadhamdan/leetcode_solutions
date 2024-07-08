class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        percent = int((s.count(letter) / len(s)) * 100)
        return percent