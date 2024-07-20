# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        
        while start < end:
            check = start + (end - start) // 2
            if isBadVersion(check):
                end = check
            else:
                start = check + 1
        return start
    
