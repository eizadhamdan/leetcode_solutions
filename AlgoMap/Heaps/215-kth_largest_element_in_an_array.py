import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # while k != 1:
        #     nums.remove(max(nums))
        #     k -= 1
        # return max(nums)

        return heapq.nlargest(k, nums)[-1]
        