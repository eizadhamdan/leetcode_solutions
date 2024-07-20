class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = len(nums)
        x = [1] * a
        for i in reversed(range(a)):
            for j in range(i, a):
                if nums[j] > nums[i]:
                    x[i] = max(x[i], 1 + x[j])
        return max(x)
    