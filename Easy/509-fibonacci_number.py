class Solution:
    def fib(self, n: int) -> int:
        # if n == 0 or n == 1:
        #     return n
        # return self.fib(n - 1) + self.fib(n - 2)

        memo = {0: 0, 1: 1}

        if n in memo:
            return memo[n]
        else:
            memo[n] = self.fib(n-1) + self.fib(n-2)
            return memo[n]