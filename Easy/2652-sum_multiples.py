class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans = []
        for i in range(1, n + 1):
            if i % 3 == 0:
                ans.append(i)
            elif i % 5 == 0:
                ans.append(i)
            elif i % 7 == 0:
                ans.append(i)
        return sum(ans)
    