class Solution
{
public:
    string reverseWords(string s)
    {
        std::istringstream iss(s);
        std::string word;
        std::vector<std::string> words;

        while (iss >> word)
        {
            words.push_back(word);
        }

        std::string reversed = "";
        for (int i = words.size() - 1; i >= 0; i--)
        {
            reversed += words[i];
            if (i != 0)
            {
                reversed += " ";
            }
        }

        return reversed;
    }
};