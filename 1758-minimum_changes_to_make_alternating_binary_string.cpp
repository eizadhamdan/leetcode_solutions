class Solution {
public:
    int minOperations(string s) {
        int n = s.length();
        int count1 = 0, count2 = 0;

        // Case 1: Pattern "010101..."
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0 && s[i] != '0') count1++;
            if (i % 2 == 1 && s[i] != '1') count1++;
        }

        // Case 2: Pattern "101010..."
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0 && s[i] != '1') count2++;
            if (i % 2 == 1 && s[i] != '0') count2++;
        }

        // Return the minimum count of changes
        return std::min(count1, count2);
    }
};