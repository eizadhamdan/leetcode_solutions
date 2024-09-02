class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        i, curr_sum, n = 0, 0, len(s)
        while i < n:
            if i < n - 1 and symbols[s[i]] < symbols[s[i+1]]:
                curr_sum += symbols[s[i+1]] - symbols[s[i]]
                i += 2
            else:
                curr_sum += symbols[s[i]]
                i += 1
        
        return curr_sum
