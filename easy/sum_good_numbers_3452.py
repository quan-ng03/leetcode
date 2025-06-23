def sumOfGoodNumbers(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    """
        Brute force:
        - Set a for loop that checks all the conditions each iteration
        - Use if/elif condition to check.
        """
    totalSum = 0
    for i in range(len(nums)):
        # Check when i-k does not exist, only i+k does
        if i - k < 0 and i + k <= len(nums) and nums[i] > nums[i + k]:
            totalSum += nums[i]
        # Check when i+k does not exist, only i-k does
        elif i - k >= 0 and i + k >= len(nums) and nums[i] > nums[i - k]:
            totalSum += nums[i]
        # Check when both cases exist and satisfy the conditions
        elif (
            i - k >= 0
            and i + k < len(nums)
            and nums[i] > nums[i - k]
            and nums[i] > nums[i + k]
        ):
            totalSum += nums[i]
    return totalSum
