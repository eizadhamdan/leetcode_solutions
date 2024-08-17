# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         if len(nums) == len(set(nums)):
#             return False
#         return True

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = set()

        for num in nums:
            if num in h:
                return True
            else:
                h.add(num)
        return False