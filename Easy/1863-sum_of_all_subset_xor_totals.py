class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def generate_subsets(nums):
            subsets = []
            for r in range(len(nums) + 1):
                subsets.extend(combinations(nums, r))
            return subsets

        subsets = generate_subsets(nums)
        xor_sum = 0

        for subset in subsets:
            xor_value = 0
            for num in subset:
                xor_value ^= num
            xor_sum += xor_value

        return xor_sum
    