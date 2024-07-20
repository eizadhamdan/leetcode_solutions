class Solution:
    def countOrders(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: 0 pairs, 1 way to arrange them (do nothing)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] * i * (2 * i - 1)

        return dp[n] % ((10 ** 9) + 7)
    