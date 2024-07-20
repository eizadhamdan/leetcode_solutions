class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        double current = 0;
        double total = 0;

        for (vector<int> customer : customers) {
            if (current < customer[0]) {
                current = customer[0];
            }

            current += customer[1];
            total += (double)(current - customer[0]);
        }

        return total / customers.size();
    }
};
