class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        operations = []

        for i in range(n):
            count = 0
            for j in range(n):
                if boxes[j] == '1' and i != j:
                    count += abs(j - i)
            operations.append(count)

        return operations
    