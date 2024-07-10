class Solution:
    def minOperations(self, logs: List[str]) -> int:
        inside = 0
        for instruction in logs:
            if len(instruction) == 2 and instruction[0] == '.':
                continue
            elif instruction[0] == '.':
                if inside == 0:
                    continue
                else:
                    inside -= 1
            else:
                inside += 1
        return inside