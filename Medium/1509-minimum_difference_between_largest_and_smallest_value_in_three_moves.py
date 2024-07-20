class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
        n = len(nums)

        return min(nums[n-1] - nums[3],             #remove three smallest elements
                   nums[n-2] - nums[2],             #remove two smallest and two largest
                   nums[n-3] - nums[1],             #remove the smallest and the two largest
                   nums[n-4] - nums[0])             #remove the three largest elements
    