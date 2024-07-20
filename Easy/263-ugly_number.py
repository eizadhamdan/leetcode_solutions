class Solution:
    def isUgly(self, n: int) -> bool:
        factors_list = [2, 3, 5]

        for factor in factors_list:
            while n > 1 and n % factor == 0:
                n = n // factor

        if n == 1:
            return True

        return False