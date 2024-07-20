class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lucky_nums = []
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        
        min_in_rows = [min(row) for row in matrix]
        
        max_in_cols = [max(col) for col in zip(*matrix)]
        
        for i in range(n_rows):
            for j in range(n_cols):
                if matrix[i][j] == min_in_rows[i] and matrix[i][j] == max_in_cols[j]:
                    lucky_nums.append(matrix[i][j])
        
        return lucky_nums
    