class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        total = 0
        total += min(prices)
        prices.remove(min(prices))
        total += min(prices)

        if money - total >= 0:
            return money - total
        return money  