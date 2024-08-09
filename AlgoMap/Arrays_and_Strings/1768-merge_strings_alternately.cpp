class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int i = 0;
        int j = 0;
        std::string ans = "";
        int word1_len = word1.length();
        int word2_len = word2.length();
        while (i < word1_len && j < word2_len) {
            ans += word1[i];
            ans += word2[j];
            i++;
            j++;
        }
        while (i < word1_len) {
            ans += word1[i++];
        }

        while (j < word2_len) {
            ans += word2[j++];
        }
        return ans;
    }
};