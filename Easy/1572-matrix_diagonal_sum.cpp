class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int n = mat.size();
        int sum_diagonal = 0;

        for (int i = 0; i < n; i++) {
            sum_diagonal += mat[i][i];
            sum_diagonal += mat[i][n - 1 - i];
        }

        if (n % 2 == 1) {
            sum_diagonal -= mat[n / 2][n / 2];
        }

        return sum_diagonal;
    }
};
