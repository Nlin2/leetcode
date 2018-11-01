"""
constraints: can't convert x to string
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # return val, xCopy to be mutable, x to be used as a check in the end
        val = 0
        xCopy = x

        # all negative values are False
        if x < 0:
            return False

        # covert int to a list of the digits
        lstDigit = []
        while xCopy // 10 != 0:
            lstDigit.append(xCopy % 10)
            xCopy = xCopy // 10
        else:
            lstDigit.append(xCopy % 10)

        # This reverses and combines the digits together
        for i, e in reversed(list(enumerate(lstDigit[::-1]))):
            val += e * 10 ** i

        if val == x:
            return True
        return False
