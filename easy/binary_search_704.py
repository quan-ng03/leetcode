""" """


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l = 0
    r = len(nums) - 1
    while l <= r:
        x = (l + r) // 2
        if nums[x] == target:
            return x
        elif nums[x] > target:
            r = x - 1
        elif nums[x] < target:
            l = x + 1
    return -1
