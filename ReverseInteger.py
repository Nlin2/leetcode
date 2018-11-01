class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        LOWER_INTERVAL = -1 * 2 ** 31
        UPPER_INTERVAL = 2 ** 31 - 1
        if x >= LOWER_INTERVAL and x <=  UPPER_INTERVAL:
            if x >= 0:
                val = int(''.join(list(str(x))[::-1]))
                if val <=  UPPER_INTERVAL:
                    return val
                return 0
            val = int('-' + ''.join(list(str(x)[1:])[::-1]))
            if val >= LOWER_INTERVAL:
                return val
        return 0
