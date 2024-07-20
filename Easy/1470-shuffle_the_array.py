class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        var = []
        for i in range(n):
            var.append(nums[i])
            var.append(nums[i-n])
        return var
