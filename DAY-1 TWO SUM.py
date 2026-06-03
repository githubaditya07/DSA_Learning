"""DAY 1
TWO SUM"""

"""LEETCODE PROBLEM 1: TWO SUM
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target."""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                find=target-nums[i]
                if nums[j]==find:
                    return[i,j]