class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = 0;
        int column = matrix[0].size() - 1;

        while(row < matrix.size() && column > -1) {
            int curr = matrix[row][column];
            if(curr == target) {
                return true;
            }
            if(target > curr) {
                row++;
            }
            else {
                column--;
            }
        }
        return false;
    }
};