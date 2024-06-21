class Solution:
    def minimumChairs(self, s: str) -> int:
        ans = chairs = 0
        for chair in s:
            chairs += 1 if chair == 'E' else -1
            ans = max(ans,chairs)
        return ans