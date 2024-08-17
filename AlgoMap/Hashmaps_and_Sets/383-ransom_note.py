class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = Counter(magazine)

        for s in ransomNote:
            if freq[s] == 0:
                return False
            freq[s] -= 1
        return True
    