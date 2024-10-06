class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        length = len(nums)
        ans = []
        i = 0
        while i < length:
            start = nums[i]

            while i < length - 1 and nums[i] + 1 == nums[i+1]:
                i += 1
            
            if start != nums[i]:
                ans.append(f"{start}->{nums[i]}")
            else:
                ans.append(str(nums[i]))

            i += 1

        return ans