class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> max_row(n, 0);
        vector<int> max_col(n, 0);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                max_row[i] = max(max_row[i], grid[i][j]);
                max_col[j] = max(max_col[j], grid[i][j]);
            }
        }

        int max_increase = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int allowed_increase = min(max_row[i], max_col[j]);
                max_increase += (allowed_increase - grid[i][j]);
            }
        }

        return max_increase;
    }
};
