class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        length = len(nums)
        if length == 1:
            return True

        first_ptr, second_ptr = 0, 1
        while second_ptr <= length - 1:
            if (nums[first_ptr] % 2) == (nums[second_ptr] % 2):
                return False
            first_ptr += 1
            second_ptr += 1

        return True
    