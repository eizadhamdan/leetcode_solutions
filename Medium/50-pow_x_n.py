class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        product = 1.0
        if n > 0:
            for _ in range(n):
                product = product * x
            
        else:
            for _ in range(-n):
                product = product * (1 / x)

        return product
    