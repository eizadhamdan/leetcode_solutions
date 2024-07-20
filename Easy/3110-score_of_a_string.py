class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        ptr1, ptr2 = 0, 1
        while ptr2 < len(s):
            score += (abs(ord(s[ptr1]) - ord(s[ptr2])))
            ptr1 += 1
            ptr2 += 1
        return score
        