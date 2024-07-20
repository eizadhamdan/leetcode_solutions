class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        seen_map = {}
        count = 0

        for hour in hours:
            remainder = hour % 24
            complement = (24 - remainder) % 24
            if complement in seen_map:
                count += seen_map[complement]
            seen_map[remainder] = seen_map.get(remainder, 0) + 1

        return count