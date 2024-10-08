class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        int count = 0;
        int index = 0;

        if (ruleKey == "type") {
            index = 0;
        }
        else if (ruleKey == "color") {
            index = 1;
        }
        else if (ruleKey == "name") {
            index = 2;
        }

        for (auto row : items) {
            if (row[index] == ruleValue) {
                count += 1;
            }
        }

        return count;
    }
};
