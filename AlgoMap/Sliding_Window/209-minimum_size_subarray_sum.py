class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        curr_sum, left_index, ans = 0, 0, len(nums)

        for right_index, val in enumerate(nums):
            curr_sum += val
            while curr_sum >= target:
                curr_sum -= nums[left_index]
                ans = min(ans, right_index - left_index + 1)
                left_index += 1

        return ans
    