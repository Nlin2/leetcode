"""
Currently Unsolved
constraints: run time should be O(log(m + n))

Ideas: 
    Median 
        issues: run time is O(1)
        Code: ---------------
        def median(lst):
            if len(lst) % 2 == 1:
                return lst[len(lst) // 2]
            return (lst[len(lst//2)] + lst[len(lst//2) + 1]) / 2
    binary search
        issues: run time is O(1) because arrays are sorted
            how about a shittier binary search where the pivot is at .75 of len
    iterations - remove both sides - counting till mid
        issues: run time is O(m + n)
    Cheese - run a for loop for O(log(m + n)) than use the median to find it
    
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        logmn = len(nums1) + len(nums2)
        # Cheese solution
        for _ in range(len(nums1) + len(nums2))
        # Used to find the search value in the binary search
        def median(lst):
            if len(lst) % 2 == 1:
                return lst[len(lst) // 2]
            return (lst[len(lst//2)] + lst[len(lst//2) + 1]) / 2

