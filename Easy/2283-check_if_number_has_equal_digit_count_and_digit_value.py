class Solution:
    def digitCount(self, num: str) -> bool:
        frequency = {}
        for char in num:
            if char not in frequency:
                frequency[char] = 1
            else:
                frequency[char] += 1
        for i in range(len(num)):
            if frequency.get(str(i), 0) != int(num[i]):
                return False
        return True