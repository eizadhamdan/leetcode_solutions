class Solution:
    def averageValue(self, nums: List[int]) -> int:
        ans = []
        for num in nums:
            if num % 6 == 0:
                ans.append(num)
        if len(ans) == 0:
            return 0
        return int(sum(ans) / len(ans))