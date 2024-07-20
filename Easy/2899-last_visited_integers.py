class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen, ans = [], []
        k = 0

        for num in nums:
            if num != -1:
                k = 0

            if num > 0:
                seen.insert(0, num)
            elif num == -1:
                k += 1
                if k > len(seen):
                    ans.append(-1)
                else:
                    ans.append(seen[k - 1])
        
        return ans
    