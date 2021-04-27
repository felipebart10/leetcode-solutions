"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

# # # APPROVED SOLUTION # # #
def moveZeroes(nums):
    if sum(nums) != 0: 
        i = 0
        j = len(nums) - 1
        """
            For each iteration, the function will check if value at position i is 0.
            If it is, then it will check if all values after it are 0 too.
            If there is a value that is not zero after it, then it will delete the position i 0
            and append it to the end of the list.
        """
        while i < j:
            if nums[i] == 0:
                while j > i:
                    if nums[j] == 0:
                        j -= 1
                    else:
                        del nums[i]
                        nums.append(0)
                        break
                
            else:
                i += 1

    return nums

nums = [1,3,2,0,3,0,1,0,0,14,0,11,2,1,3,0,0,0,0,31,31,34]

print(moveZeroes(nums))