"""
#1
runtime min: 36 ms
optimal solution
Date: 10/14/18

Problem: Given a positive integer N, find and return the longest distance
between two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.
"""
class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int

        >>> binaryGap(22)
        2
        >>> binaryGap(5)
        2
        >>> binaryGap(6)
        1
        >>> binaryGap(8)
        0
        """
        b = list(bin(N))[2:]
        indices = [i for i, elem in enumerate(b) if elem == "1"]
        max_len = 0
        for i in range(len(indices) - 1):
            length = indices[i+1] - indices[i]
            if length > max_len:
                max_len = length
        return max_len
