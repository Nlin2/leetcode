"""
#2
Date: 10/14/18

Problem:
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not
use the same element twice

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # dictionary/hash of the values seen
        parsed_nums = {}
        # iterate through nums
        for i, num in enumerate(nums):
            # the complement is the missing complement of one of the two sums
            complement = target - num
            # if the complement exists, success
            if complement in parsed_nums:
                return [parsed_nums.get(complement), i]
            # if the complement does not exist, the nums are stored as 
            # complement numbers for other numbers
            parsed_nums[num] = i

