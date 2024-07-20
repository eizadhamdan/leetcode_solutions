class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []

        for _ in range(len(nums) // 2):
            minimum = min(nums)
            maximum = max(nums)
            averages.append((minimum + maximum) / 2)
            nums.remove(minimum)
            nums.remove(maximum)
        
        return min(averages)
    