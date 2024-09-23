class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        const int EMPTY = 0, FRESH = 1, ROTTEN = 2;
        int rows = grid.size();
        int cols = grid[0].size();
        int num_fresh = 0;
        queue<pair<int, int>> q;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == ROTTEN) {
                    q.push({i, j});
                } 
                else if (grid[i][j] == FRESH) {
                    num_fresh++;
                }
            }
        }

        if (num_fresh == 0) return 0;

        int num_minutes = -1;

        while (!q.empty()) {
            int q_size = q.size();
            num_minutes++;

            for (int k = 0; k < q_size; k++) {
                auto pos = q.front();
                q.pop();
                int i = pos.first, j = pos.second;
                for (auto dir : vector<vector<int>>{{0,1},{1,0},{0,-1},{-1,0}}) {
                    int r = i + dir[0], c = j + dir[1];
                    if (r >= 0 && r < rows && c >= 0 && c < cols && grid[r][c] == FRESH) {
                        grid[r][c] = ROTTEN;
                        num_fresh--;
                        q.push({r, c});
                    }
                }
            }
        }

        if (num_fresh == 0) return num_minutes;
        
        return -1;
    }
};