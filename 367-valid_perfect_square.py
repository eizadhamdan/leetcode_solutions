class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if (int(num ** 0.5)) ** 2 == num:
            return True
        return False