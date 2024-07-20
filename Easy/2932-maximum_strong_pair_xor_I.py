class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        max_xor = 0
        for x in nums:
            for y in nums:
                if abs(x - y) <= min(x, y):
                    xor = x ^ y
                    if max_xor < xor:
                        max_xor = xor
        return max_xor
