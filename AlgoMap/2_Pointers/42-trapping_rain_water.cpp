class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() == 0 || height.size() == 1) return 0;
        //use two pointers
        int left = 0;
        int right = height.size() - 1;
        int left_max = 0;
        int right_max = 0;
        int total_water = 0;

        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= left_max) {
                    left_max = height[left];
                }
                else {
                    total_water += (left_max - height[left]);
                }
                left++;
            }
            else {
                if (height[right] >= right_max) {
                    right_max = height[right];
                }
                else {
                    total_water += (right_max - height[right]);
                }
                right--;
            }
        }
        return total_water;
    }
};
