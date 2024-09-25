class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen_nums = set()
        sneaky_nums = []
        for num in nums:
            if num in seen_nums:
                seen_nums.add(num)
                sneaky_nums.append(num)
            else:
                seen_nums.add(num)
        return sneaky_nums
