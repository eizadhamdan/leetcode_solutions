class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        # n = len(nums)
        # for i in range(n):
        #     for j in range(n):
        #         if str(bin(nums[i] | nums[j]))[-1] == '0' and i != j:
        #             return True
        # return False

        """Alternative"""
        evens = 0
        for num in nums:
            if not num & 1:
                evens += 1
                if evens >= 2:
                    return True
        return False