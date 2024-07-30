class Solution {
public:
    int xorBeauty(vector<int>& nums) {
        int a = 0, b = 0;
        for(auto &i: nums){
            a |= i;  // Accumulate OR of all numbers
            b ^= i;  // Accumulate XOR of all numbers
        }
        return (a & b);     //return AND
    }
};