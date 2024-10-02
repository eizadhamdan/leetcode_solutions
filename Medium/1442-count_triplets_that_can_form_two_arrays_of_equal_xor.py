class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefixXOR = [0] * (n + 1)
        
        for i in range(n):
            prefixXOR[i + 1] = prefixXOR[i] ^ arr[i]
        
        count = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                if prefixXOR[i] == prefixXOR[j + 1]:
                    count += (j - i)
        return count