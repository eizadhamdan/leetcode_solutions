class Solution {
public:
    int numberOfChild(int n, int k) {
        int direction = 1;
        int i = 0;
        while (k != 0) {
            i += direction;
            k--;
            if (i == n - 1 || i == 0) {
                direction *= -1;
            }
        }
        return i;
    }
};