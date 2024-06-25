class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors_list = []
        for i in range(1, n+1):
            if n % i == 0:
                factors_list.append(i)
                
        if k <= len(factors_list):
            return factors_list[k - 1]
        else:
            return -1
        