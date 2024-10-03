class Solution
{
public:
    void rotate(vector<int> &nums, int k)
    {
        int length = nums.size();
        k = k % length;
        int left = 0;
        int right = length - 1;

        while (left < right)
        {
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left++;
            right--;
        }

        left = 0;
        right = k - 1;
        while (left < right)
        {
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left++;
            right--;
        }

        left = k;
        right = length - 1;
        while (left < right)
        {
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left++;
            right--;
        }
    }
};