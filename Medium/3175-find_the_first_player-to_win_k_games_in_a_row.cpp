class Solution {
public:
    int findWinningPlayer(vector<int>& skills, int k) {
        int n = skills.size();
        int first_player = 0;
        int second_player = 1;
        int wins = 0;
        for (int second_player = 1; second_player < n; second_player++) {
            if (skills[first_player] < skills[second_player]) {
                wins = 0;
                first_player = second_player;
            }
            wins++;
            if (wins == k) break;
        }
        return first_player;
    }
};