class Solution:
    def countDigits(self, num: int) -> int:
        n = str(num)
        total = 0
        for i in n:
            if num % int(i) == 0:
                total += 1
        return total
    