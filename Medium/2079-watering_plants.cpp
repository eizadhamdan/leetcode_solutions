class Solution {
public:
    int wateringPlants(vector<int>& plants, int capacity) {
        int steps = 0;
        int current_capacity = capacity;

        for (int i = 0; i < plants.size(); i++) {
            if (current_capacity < plants[i]) {
                steps += 2 * i;
                current_capacity = capacity;
            }
            steps++;
            current_capacity -= plants[i];
        }

        return steps;
    }
};
