class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        twice_nums = [k for k, v in freq.items() if v == 2]
        ans = 0
        for num in twice_nums:
            ans ^= num
        return ans