class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {
        // int count = 0;
        // for (int i = 0; i < sentences.size(); i++) {
        //     int word_count = 0;
        //     for (int j = 0; j < sentences[i].length(); j++) {
        //         if (sentences[i][j] == ' ') word_count++;
        //     }
        //     if (word_count > count) count = word_count;
        // }
        // return count + 1;

        int maxWords = 0;

        for (const string& sentence : sentences) {
            stringstream ss(sentence);
            int wordCount = 0;
            string word;

            while (ss >> word) {
                ++wordCount;
            }

            maxWords = max(maxWords, wordCount);
        }

        return maxWords;
    }
};