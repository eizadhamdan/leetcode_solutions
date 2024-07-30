class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)

        sorted_characters = sorted(frequency.items(), key=lambda item: (-item[1], s.index(item[0])))

        ans = "".join(char * count for char, count in sorted_characters)

        return ans