class Solution {
public:
    int arraySign(vector<int>& nums) {
        int negative_count = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                return 0;
            }
            if (nums[i] < 0) {
                negative_count += 1;
            }
        }
        if (negative_count % 2 == 1) {
            return -1;
        }
        return 1;
    }
};