class Solution
{
public:
    vector<int> stableMountains(vector<int> &height, int threshold)
    {
        std::vector<int> stable_mountains;
        for (int i = 1; i < height.size(); i++)
        {
            if (height[i - 1] > threshold)
            {
                stable_mountains.push_back(i);
            }
        }
        return stable_mountains;
    }
};