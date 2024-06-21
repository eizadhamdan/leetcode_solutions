class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        count = 0
        length = len(hours)
        for i in range(length):
            for j in range(i+1, length):
                if (hours[i] + hours[j]) % 24 == 0:
                    count += 1
        return count