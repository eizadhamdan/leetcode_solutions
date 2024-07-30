class Solution {
public:
    int numTeams(vector<int>& rating) {
        int n = rating.size();
        int num_teams = 0;

        // for (int i = 0; i < n; i++) {
        //     for (int j = i + 1; j < n; j++) {
        //         for (int k = j + 1; k < n; k++) {
        //             if ((rating[i] < rating[j] && rating[j] < rating[k]) || 
        //                 (rating[i] > rating[j] && rating[j] > rating[k])) {
        //                     num_teams++;
        //                 }
        //         }
        //     }
        // }

        vector<int> left_smaller(n, 0);
        vector<int> right_larger(n, 0);
        vector<int> left_larger(n, 0);
        vector<int> right_smaller(n, 0);
        
        // Calculate left_smaller and right_larger
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (rating[j] < rating[i]) {
                    ++left_smaller[i];
                }
            }
            for (int j = i + 1; j < n; ++j) {
                if (rating[j] > rating[i]) {
                    ++right_larger[i];
                }
            }
        }
        
        // Calculate left_larger and right_smaller
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (rating[j] > rating[i]) {
                    ++left_larger[i];
                }
            }
            for (int j = i + 1; j < n; ++j) {
                if (rating[j] < rating[i]) {
                    ++right_smaller[i];
                }
            }
        }
        
        // Calculate the number of valid teams
        for (int i = 0; i < n; ++i) {
            num_teams += left_smaller[i] * right_larger[i];
            num_teams += left_larger[i] * right_smaller[i];
        }
        
        return num_teams;
    }
};