class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = {}
        for num in nums:
            if num not in ans:
                ans[num] = 1
            ans[num] += 1
        return max(ans, key=ans.get)
    