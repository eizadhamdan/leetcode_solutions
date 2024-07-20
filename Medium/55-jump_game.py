class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # A greedy approach
        goal = len(nums) - 1        # last index

        for i in range(goal, -1, -1):
            max_jump = nums[i]
            if i + max_jump >= goal:
                goal = i
        
        if goal == 0:
            return True
        else:
            return False