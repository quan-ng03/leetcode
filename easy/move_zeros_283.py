"""
Utilize two pointers, one will iterate the loop, the non-zero pointer will stay at the zero. When the loop detect a non-zero, swap place with the non-zero pointer
and increment the non-zero pointer.
"""


def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    non_zero = 0  # Pointer for non-zero elements

    # Move all non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[non_zero] = nums[non_zero], nums[i]
            non_zero += 1
    return nums
