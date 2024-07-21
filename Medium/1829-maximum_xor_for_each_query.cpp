class Solution {
public:
    vector<int> getMaximumXor(vector<int>& nums, int maximumBit) {
        int ans = 0;
        for (int num : nums) {
            ans ^= num;
        }

        int right = pow(2, maximumBit) - 1;
        vector<int> answer;

        while(nums.size() != 0) {
            int k = right ^ ans;
            answer.push_back(k);
            ans = ans ^ nums[nums.size() - 1];
            nums.pop_back();
        }

        return answer;
    }
};
