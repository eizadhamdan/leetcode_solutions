class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        counter = Counter(nums)
        good_pairs = 0

        for i, num in enumerate(nums):
            counter[num] -= 1
            good_pairs += counter[num]

        return good_pairs