class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int first = 0;
        int second = numbers.size() - 1;

        while (first < second) {
            int sum = numbers[first] + numbers[second];
            if (sum == target) {
                return {first + 1, second + 1};
            } 
            else if (sum < target) {
                ++first;
            } 
            else {
                --second;
            }
        }
        return {};
    }
};