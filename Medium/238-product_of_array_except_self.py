class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prodFromLeft = [0] * n
        prodFromRight = [0] * n
        left = 1
        right = 1

        for i, num in enumerate(nums):
            prodFromLeft[i] = left
            j = - i - 1
            prodFromRight[j] = right
            left *= nums[i]
            right *= nums[j]

        return [l * r for l, r in zip(prodFromLeft, prodFromRight)]
    