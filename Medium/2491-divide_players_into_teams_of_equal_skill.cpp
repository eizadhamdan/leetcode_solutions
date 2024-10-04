class Solution
{
public:
    long long dividePlayers(vector<int> &skill)
    {
        int len = skill.size();
        sort(begin(skill), end(skill));
        long ans = 0, target = skill[0] + skill[len - 1], val1, val2;

        int i = 0, j = len - 1;
        while (i < j)
        {
            val1 = skill[i++];
            val2 = skill[j--];
            if (val1 + val2 != target)
                return -1;
            ans += (val1 * val2);
        }
        return ans;
    }
};