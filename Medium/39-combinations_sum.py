class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(candidates)

        def backtrack(index, curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return
            if curr_sum > target or index == n:
                return

            backtrack(index+1, curr_sum)

            sol.append(candidates[index])
            backtrack(index, curr_sum+candidates[index])
            sol.pop()

        backtrack(0, 0)
        return res
