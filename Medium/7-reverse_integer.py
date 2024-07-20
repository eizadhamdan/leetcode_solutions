class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x >= 0):
            string = str(x)
            string = string[::-1]
            integer = int(string)
            if integer > pow(2, 31) - 1:
                return 0
            return integer
        else:
            x *= -1
            string = str(x)
            string = string[::-1]
            integer = int(string)
            integer *= -1
            if integer < -1 * pow(2, 31):
                return 0
            return integer
        