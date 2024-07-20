class Solution {
public:
    int returnToBoundaryCount(vector<int>& nums) {
        int location = nums[0];
        int boundary = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (location == 0) {
                boundary += 1;
            }
            location += nums[i];
        }
        if (location == 0) boundary += 1;
        return boundary;
    }
};
