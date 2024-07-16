class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        vector<int> arr;

        int x = 0;
        for (int i = 0; i < pref.size(); i++) {
           arr.push_back(pref[i] ^ x);
           x = pref[i]; 
        }

        return arr;
    }
};
