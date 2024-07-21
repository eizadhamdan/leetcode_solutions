class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        #The max digit in the number determines the minimum number of deci-binary numbers
        #needed. 
        #This is because each deci-binary number can contribute at most 1 to any given
        #placevalue.

        # n = list(n)
        return int(max(n))
    