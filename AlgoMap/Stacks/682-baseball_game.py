class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        if len(operations) == 0:
            return 0

        for operation in operations:
            if operation == 'C':
                ans.pop()
            elif operation == 'D':
                ans.append(2 * ans[-1])
            elif operation == '+':
                ans.append(ans[-1] + ans[-2])
            else:
                ans.append(int(operation))
        return sum(ans)