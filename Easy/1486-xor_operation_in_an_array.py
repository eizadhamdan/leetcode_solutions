class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        total = 0
        for i in range(n):
            total ^= (start + 2 * i)
        return total
    