class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
        vector<int> total;
        for (int i = 0; i < prices.size(); i++) {
            bool set = false;
            for (int j = i + 1; j < prices.size(); j++) {
                if (prices[j] <= prices[i]) {
                    total.push_back(prices[i] - prices[j]);
                    set = true;
                    break;
                }
            }
            if (!set) {
                total.push_back(prices[i]);
            }
        }

        return total;
    }
};
