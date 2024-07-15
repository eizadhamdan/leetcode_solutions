class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0

        for i in range(len(moves)):
            move = moves[i]

            if move == 'U':
                y -= 1
            elif move == 'D':
                y += 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
        return x == 0 and y == 0
    