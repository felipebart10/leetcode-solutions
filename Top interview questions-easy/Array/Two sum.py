"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
"""

# This funciton will run through the list, checking if the list has an element that
# is equal to 'number2', which is the 'target' minus the current elemnent tested.
# it also checks if both numbers are in the same position, a restriction

# APPROVED SOLUTION
def twoSum(nums, target):
    for num in nums:
        number2 = target - num

        # this will return if number2 is in nums and will restrict
        if number2 in nums and nums.index(num) != nums.index(number2):
            return [nums.index(num), nums.index(number2)]

        # this will test if the solution is composed of two elements with the same value
        # and returns both indexes, using list comprehension and enumerate
        elif len([i for i,x in enumerate(nums) if x==num]) > 1 and num * 2 == target:
            return [i for i,x in enumerate(nums) if x==num]
