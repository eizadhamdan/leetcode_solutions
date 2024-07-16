class Solution {
public:
    int differenceOfSum(vector<int>& nums) {
        int element_sum = 0;
        int digit_sum = 0;

        for (int i = 0; i < nums.size(); i++) {
            element_sum += nums[i];

            int n = nums[i];
            while(n != 0) {
                int rem = n % 10;
                n = n / 10;
                digit_sum += rem;
            }
        }

        return abs(digit_sum - element_sum);
    }
};
