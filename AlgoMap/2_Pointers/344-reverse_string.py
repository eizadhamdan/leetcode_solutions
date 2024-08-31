class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        num = len(s) // 2
        for i in range(num):
            extra = s[i]
            s[i] = s[n-i-1]
            s[n-i-1] = extra
        
        return s