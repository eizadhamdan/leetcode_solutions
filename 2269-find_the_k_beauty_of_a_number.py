class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num = str(num)
        beauty = 0
        for i in range(len(num)-k+1):
            try:
                if int(num) % int(num[i:i+k]) == 0:
                    beauty += 1
            except ZeroDivisionError:
                continue
        return beauty