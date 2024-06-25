class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dictionary = {}
        maxFreq = 0

        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1

            maxFreq = max(maxFreq, dictionary[num])

        result = 0
        for _, value in dictionary.items():
            if value == maxFreq:
                result += value
        return result