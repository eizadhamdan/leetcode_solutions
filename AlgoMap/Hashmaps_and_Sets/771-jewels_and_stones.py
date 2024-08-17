class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq_stones = Counter(stones)
        
        num = 0
        for jewel in jewels:
            if jewel in freq_stones:
                num += freq_stones[jewel]
        return num
    