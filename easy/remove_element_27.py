def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    # The problem main issue is to solve it in-place, meaning that i cannot create a new object but to make changes on the existing one.
    # My solution is to create two pointers, one at the beginning and the other at the end of the list.
    # If the value at the beginning is equal to the target value, then I swap the values of the two pointers and move the end pointer one step to the left.
    # If the value at the beginning is not equal to the target value, then I move the beginning pointer one step to the right.
    # I repeat the process until the beginning pointer is greater than the end pointer. This should cover the case where when two pointers are equal and the value
    # is not equal to the target value, it still counts.
    # The time complexity of this solution is O(n) and the space complexity is O(1).

    i = 0
    j = len(nums) - 1
    while i <= j:
        if nums[i] == val:
            nums[i], nums[j], j = nums[j], nums[i], j - 1
        else:
            i += 1
    return i
