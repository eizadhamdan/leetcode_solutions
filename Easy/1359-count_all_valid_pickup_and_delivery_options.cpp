class Solution {
public:
    int countOrders(int n) {
        int mod = 1e9 + 7;
        long long box = 2 * n;
        long long res = 1;

        for (int i = 0; i < n; i++) {
            res = res * ((box * (box - 1)) / 2) % mod;
            box -= 2;
        }
        return (int)res;
    }
};



/* We have 2n tasks, n deliveries and n pickups */

/*
Python code using dynamic programming-------------

class Solution:
    def countOrders(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: 0 pairs, 1 way to arrange them (do nothing)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] * i * (2 * i - 1)

        return dp[n] % ((10 ** 9) + 7)




*/