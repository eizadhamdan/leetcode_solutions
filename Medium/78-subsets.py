class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol_list = list()
        return_list = list()
        n = len(nums)

        def backtrack(i=0):
            if i == n:
                return_list.append(sol_list[:])
                return
            
            backtrack(i+1)

            sol_list.append(nums[i])
            backtrack(i+1)
            sol_list.pop()


        backtrack()
        return return_list
    