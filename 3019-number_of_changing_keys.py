class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        changes = 0
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                changes += 1
        return changes
    