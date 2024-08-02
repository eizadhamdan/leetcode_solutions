class Solution {
public:
    int valueAfterKSeconds(int n, int k) {
        vector<int> a(n, 1);
        int MOD = 1e9 + 7;

        while (k > 0) {
            vector<int> prefixSum(n);
            prefixSum[0] = a[0];
            for (int i = 1; i < n; i++) {
                prefixSum[i] = (prefixSum[i - 1] + a[i]) % MOD;
            }
            for (int i = 1; i < n; i++) {
                a[i] = (a[i] + prefixSum[i - 1]) % MOD;
            }
            k--;
        }
        return a[n - 1] % MOD;
    }
};