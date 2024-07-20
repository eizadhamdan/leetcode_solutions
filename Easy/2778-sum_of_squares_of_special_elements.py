class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        specials = []
        for i in range(n):
            if n % (i + 1) == 0:
                specials.append(nums[i] ** 2)
        return sum(specials)
