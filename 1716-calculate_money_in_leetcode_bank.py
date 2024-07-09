class Solution:
    def totalMoney(self, n: int) -> int:
        times = n // 7
        rem = n % 7
        total = 0
        start = 1
        for _ in range(times):
            for j in range(start, start + 7):
                total += j
            start += 1
        for i in range(start, start + rem):
            total += i
        return total