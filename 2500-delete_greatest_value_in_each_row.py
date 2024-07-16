class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        total = 0
        while grid[0]:
            max_in_row = []
            for row in grid:
                maximum = max(row)
                max_in_row.append(maximum)
                row.remove(maximum)
            total += max(max_in_row)
        
        return total
    