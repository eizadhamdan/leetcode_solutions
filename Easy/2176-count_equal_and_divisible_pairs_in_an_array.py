class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pairs = 0
        for i in range(n):
            for j in range(n):
                if nums[i] == nums[j] and (i * j) % k == 0 and i < j:
                    pairs += 1
        return pairs