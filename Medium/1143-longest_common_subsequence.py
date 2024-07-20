class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        a, b = len(text1), len(text2)
        x = [[0] * (b + 1) for _ in range(a + 1)]
        for i in reversed(range(a)):
            for j in reversed(range(b)):
                if text1[i] == text2[j]:
                    x[i][j] = x[i + 1][j + 1] + 1
                else:
                    x[i][j] = max(x[i + 1][j], x[i][j + 1])
        return x[0][0]
    