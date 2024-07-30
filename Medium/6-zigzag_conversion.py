class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        matrix = [[] for _ in range(numRows)]
        
        direction = 1
        start = 0
        ptr = 0

        while(ptr < len(s)):
            matrix[start].append(s[ptr])
            start += direction
            ptr += 1

            if start == 0 or start == numRows - 1:
                direction *= -1
        
        result = ''.join([''.join(row) for row in matrix])

        return result
    