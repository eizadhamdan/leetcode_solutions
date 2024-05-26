class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # for _ in range(len(nums)):
        #     nums.append(nums[_])
        # return nums

        length = len(nums)
        for i in range(length):
            nums.append(nums[i])
        return nums