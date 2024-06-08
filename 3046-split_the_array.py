class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = Counter(nums)         # for frequency of each integer(it is a dictionary)

        for frequency in counter.values():
            if frequency > 2:           # can't split in two
                return False
        return True