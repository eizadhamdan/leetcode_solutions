class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]

        for _ in range(1, numRows):
            row = [1]
            for i in range(1, len(rows[-1])):
                row.append(rows[-1][i-1] + rows[-1][i])
            row.append(1)
            rows.append(row)
        
        return rows