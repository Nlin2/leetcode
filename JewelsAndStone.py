"""
#3
"""
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return len(list(filter(lambda c: c in J, list(S))))
