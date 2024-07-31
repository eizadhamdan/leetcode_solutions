class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams = 0
        prev = 0

        for row in bank:
            count = row.count('1')
            if count:
                beams += prev * count
                prev = count
        
        return beams
    