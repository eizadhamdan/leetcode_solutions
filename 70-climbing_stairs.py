class Solution:
    # @cache
    # def climbStairs(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     if n == 2:
    #         return 2

    #     one_back = self.climbStairs(n - 1)
    #     two_back = self.climbStairs(n - 2)

    #     return one_back + two_back

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        one_back = 2
        two_back = 1
        for i in range(2, n):
            next_num = two_back + one_back
            two_back = one_back
            one_back = next_num

        return one_back
