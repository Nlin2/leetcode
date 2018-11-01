class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rmnNm = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        val = 0
        for i in range(len(s) - 1):
            if rmnNm[s[i]] < rmnNm[s[i + 1]]:
                val -= rmnNm[s[i]]
            else:
                val += rmnNm[s[i]]
        return val + rmnNm[s[-1]]          

