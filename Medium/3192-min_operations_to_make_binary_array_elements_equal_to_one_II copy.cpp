class Solution {
public:
    int minOperations(vector<int>& nums) {
        int flipped = 0;
        int ans = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == flipped % 2) {
                flipped++;
                ans++;
            }
        }
        return ans;
    }
};