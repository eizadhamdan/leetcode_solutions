class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int operations = 0;

        for(int i = 0; i < nums.size(); i++) {
            int rem = nums[i] % 3;
            if (rem != 0) {
                operations += min(3 - (rem), rem);
            }
        }
        return operations;
    }
};
