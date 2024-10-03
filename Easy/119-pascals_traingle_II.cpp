class Solution
{
public:
    vector<int> getRow(int rowIndex)
    {
        vector<int> row(rowIndex + 1, 1);
        long long mul = 1;
        for (int i = 1; i < rowIndex; i++)
        {
            mul *= (rowIndex + 1 - i);
            mul /= i;
            row[i] = mul;
        }
        return row;
    }
};