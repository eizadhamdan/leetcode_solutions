class Solution {
public:
    int minOperations(vector<int>& nums) {
        int flips = 0;
        int n = nums.size();

        for (int i = 0; i < n - 2; i++) {
            if (nums[i] == 0) {
                flips++;
                nums[i] = 1;
                nums[i+1] = 1 - nums[i+1];
                nums[i+2] = 1 - nums[i+2];
            }
        }

        if (nums[n-1] == 1 && nums[n-2] == 1) {
            return flips;
        }
        return -1;
    }
};